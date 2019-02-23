# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/20/2019
Project name: WUSB Donor Monitor ©

Module name: database.py
Module description:
        The reason this module is developed instead of just using gsheets is to create a system of modularity
        that will allow minimal change to be required when we switch to a local database.
'''

import gspread
from gspread import exceptions as gs_exceptions
from oauth2client.service_account import ServiceAccountCredentials
import debug as dbg
import os

class Database:
    '''
    Wrapper for GSpread api. Allows the server to interface and get data from Google Sheets
    '''

    creds = None
    '''
    GAPI credentials used to log in to Google Sheets
    '''
    gs = None
    '''
    Google sheets interface linked with GAPI credentials
    '''
    sheet = None
    '''
    Worksheet interface linked with the specified worksheet and document ID
    '''

    def __init__(self, doc_ID='', wsheet_ID=0, creds={}):
        '''
        Initialize new Database class with credentials, a document ID and a worksheet ID.

        :param doc_ID: Str: Document ID of Google Sheets document to be linked with Database class
        :param wsheet_ID: Int: Worksheet ID of Google Sheets data to access
        :param creds: ServiceAccountCredentials: Credentials used to gain permission to access Google Sheets data
        '''

        try:
            # Attempt to log into Google Sheets and make new gspread instance
            dbg.log("Attempting Google Sheets authorization...")
            self.creds = creds
            self.gs = gspread.authorize(self.creds)

            # Log Google Sheet authorization success if authorisation is successful
            dbg.success("Authorization successful")
        except:
            # Throw error if 'creds' passed are invalid
            raise ValueError("Invalid creds object passed into 'Database' constructor: " + str(creds))

        # Set document ID and worksheet ID of Database to what was passed in through constructor args
        self.set_doc(doc_ID, wsheet_ID)

    def set_doc(self, doc_ID='', wsheet_ID=0):
        '''
        Links database instance with document ID 'doc_ID' and worksheet ID 'wsheet_ID'

        :param doc_ID: Str
        :param wsheet_ID: ID
        :return: None
        '''

        try:
            # Attempt to link 'sheet' against GSheets document with ID 'doc_ID' and worksheet ID 'wsheet_ID'
            dbg.log("Attempting to link with Google Sheets document...")
            self.sheet = self.gs.open_by_key(doc_ID).get_worksheet(wsheet_ID)

            # Print success message if able to succesfully link with GSheets document
            dbg.success("Successfully linked with Google Sheets document")
        except gs_exceptions.APIError as e:
            # Throw error and exit if read permissions were not set
            if e.response.json()['error']['code'] == 403:
                dbg.err(
                    "Didn't have permissions to read Google Sheets document. " +
                    "Please make document public or create a shareable link to it.")
                input("Press any key to exit...")
                os._exit(-1)
            # Throw error and exit if document does not exist
            elif e.response.json()['error']['code'] == 404:
                dbg.err("Tried to read Google Sheets document, but the document does not exist.")
                input("Press any key to exit...")
                os._exit(-1)
            # Throw error and exit if any other bad response is received
            else:
                dbg.err("Tried to read Google Sheets document, but got the following error response instead:")
                dbg.err(e.response.text)
                input("Press any key to exit...")
                os._exit(-1)

    def get_cell(self, x=0, y=0):
        '''
        Gets data from cell at (x, y). Coords start at (0, 0).

        :param x: Int
        :param y: Int
        :return: Cell
        '''

        dbg.log("Attempting to get data at cell (" + str(x) + "," + str(y) + ")")

        # Throw error if x or y are out of range
        assert x < 1000, "Specified x coord '" + str(x) + "' is too high. x can be 999 at max because there are only 1000 rows."
        assert y < 26, "Specified y coord '" + str(y) + "' is too high. y can be 25 at max because there are only 25 columns."
        assert x >= 0, "Specified x coord '" + str(x) + "' is too low. x can be 0 at minimum."
        assert y >= 0, "Specified y coord '" + str(y) + "' is too low. y can be 0 at minimum."

        # Log success
        dbg.success("Data successfully gotten")

        # Return cell value by converting to Google Sheet coords (instead of (0, 0) being min, (1, 1) is)
        return self.sheet.cell(x + 1, y + 1)

    def find_cell(self, val=""):
        '''
        Gets data from cell with value of val. Returns none if cell cannot be found.

        :param val: Str
        :return: Cell | None
        '''

        # Throw error if val is not a Str
        assert type(val) == type(""), "'val' parameter passed '" + str(val) + "' should be Str but isn't"

        # sheet.find() throws an error if cell cannot be found, so this is handled by returning 'none'
        try:
            # Try to get cell
            dbg.log("Attempting to find cell with value '" + val + "'")
            cell = self.sheet.find(val)

            # Log success if cell if found
            dbg.success("Found cell with value '" + val + "'")

            return cell
        except gs_exceptions.CellNotFound:
            dbg.warn("Could not find cell with value '" + val + "'")
            return None

    def get_cell_loc(self, val=""):
        '''
        Gets data from cell with value of val using cartesian coordinates

        :param val: Str
        :return: Tuple with values (Int x, Int y) | None
        '''

        # Attempt to find cell with value 'val'
        cell = self.find_cell(val)

        # If cell gotten does not exist, return none
        if cell is None:
            return None
        else:
            # Return cell coords transformed to cartesian coords (1, 1) -> (0, 0)
            return (cell.col - 1, cell.row - 1)

    def get_col(self, x=0):
        '''
        Gets every value at column x. ‘x’ coord starts from 0.

        :param x: Int
        :return: List
        '''

        # Log column getting status (for lack of a better term)
        dbg.log("Attempting to get data from column " + str(x) + "...")

        # Throw error if y is out of bounds
        assert x < 26, "'y' parameter '" + str(x) + "' is too high. Must be at most 25 because there are 26 columns in a sheet."
        assert x >= 0, "'y' parameter '" + str(x) + "' is too low. Must be 0 at minimum."

        # Return data from column by converting from cartesian to GSheet coords
        data = self.sheet.col_values(x + 1)
        dbg.success("Successfully got data from column " + str(x))
        return data

    def get_row(self, y=0):
        '''
        Gets every value at row y. ‘y’ coord starts from 0.

        :param y: Int
        :return: List
        '''

        # Log row getting status (for lack of a better term)
        dbg.log("Attempting to get data from row " + str(y) + "...")

        # Throw error if y is out of bounds
        assert y < 1000, "'y' parameter '" + str(y) + "' is too high. Must be at most 999 because there are 1000 rows in a sheet."
        assert y >= 0, "'y' parameter '" + str(y) + "' is too low. Must be 0 at minimum."

        # Return data from column by converting from cartesian to GSheet coords
        data = self.sheet.row_values(y + 1)
        dbg.success("Successfully got data from row " + str(y))
        return data

    def get_range(self, p1=(0,0), p2=(0,0)):
        '''
        Gets all cells in range of the 2 tuples passed in. Returns a list of cells.

        :param p1: Tuple with values (int x, int y)
        :param p2: Tuple with values (int x, int y)
        :return: Cell[]
        '''

        # Throw error if p1 or p2 are out of range
        assert 0 <= p1[0] < 26, "p1 'x' parameter '" + str(p1[0]) + "' is out of range [0, 25]"
        assert 0 <= p2[0] < 26, "p2 'x' parameter '" + str(p2[0]) + "' is out of range [0, 25]"
        assert 0 <= p1[1] < 26, "p1 'y' parameter '" + str(p1[1]) + "' is out of range [0, 1000]"
        assert 0 <= p2[1] < 26, "p1 'y' parameter '" + str(p2[1]) + "' is out of range [0, 1000]"

        # Log range getting status (for lack of a better term)
        dbg.log("Attempting to get all cells in range (" + str(p1[0]) + ',' + str(p1[1]) + ") and (" + str(p2[0]) + ',' + str(p2[1]) + ')')

        #Get cells in range of points p1 and p2 using GSheet coords (converting from cartesian coords)
        data = self.sheet.range(p1[0] + 1, p1[1] + 1, p2[0] + 1, p2[1] + 1)

        # Log success
        dbg.success("Successfully got all cells in range (" + str(p1[0]) + ',' + str(p1[1]) + ") and (" + str(
            p2[0]) + ',' + str(p2[1]) + ')')

        return data







