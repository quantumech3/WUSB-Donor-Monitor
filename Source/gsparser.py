# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/20/2019
Project name: WUSB Donor Monitor ©

Module name: gsparser.py
Module description:
        This module contains methods for turning GSheets data into ‘Donor‘ and ‘RadiothonInfo’ data structures.
'''

import debug as dbg


def find(key, vals=[], keys=[]):
    '''
    Searches through ‘keys’ for value ‘key’ kind of like a dictionary and either returns the value in ‘vals’ associated with it,
    or if it can't find it then returns ‘None’

    :param key: Any
    :param vals: List
    :param keys: List
    :return: Any
    '''

    try:
        # Attempt to get the associated list value
        return vals[keys.index(key)]
    except IndexError:
        # Return None if the value is out of range for 'vals'
        return None
    except ValueError:
        # Return None and throw a warning if the value doesnt exist in 'keys'
        dbg.warn("gsparser.find() tried to find value for key '" + str(key) + "' that does not exist")
        return None


def to_Pledge(row=[], head=[]):
    '''
    Turns a pledge entry row from a GSheets document into a ‘Pledge’ data structure.

    :param row:
    :param head:
    :return: PledgeDict
    '''

    def lex(row=[], head=[]):
        '''
        Associates row and header with appropiate 'Donor' data structure keys
        :param row:
        :param head:
        :return: DonorDict
        '''

        # Associate GSheet values with their respective 'Pledge' data type keys
        pledge = {}
        pledge["firstName"] = find("First name", row, head)
        pledge["city"] = find("City", row, head)
        pledge["amtDonated"] = find("Amount donated", row, head)
        pledge["pledgeType"] = find("Website or Caller", row, head)
        pledge["paidByCredit"] = find("Paid by credit card?", row, head)
        pledge["isPaid"] = find("Is paid", row, head)

        # Throw errors for every column data type that could not be found
        if "First name" not in head:
            dbg.err("ALL first names of donors will NOT be displayed because the 'First name' column header does not exist.")
        if "City" not in head:
            dbg.err("ALL donor's cities will NOT be displayed because the 'City' column header does not exist.")
        if "Amount donated" not in head:
            dbg.err("ALL donation amounts will NOT be displayed because the 'Amount donated' column header does not exist.")
        if "Website or Caller" not in head:
            dbg.err("ALL pledge types (Website or Caller) will be deemed 'Website' payments because the 'Website or Caller' column header does not exist.")
        if "Paid by credit card?" not in head:
            dbg.err("ALL credit card payments will NOT be displayed because the 'Paid by credit card?' column header does not exist.")

        return pledge

    def parce(pledge={}):
        '''
        Data type casting, 'None' type substitution with 'N/A' and other parsing into correct data structures
        :param pledge: PledgeDict
        :return: PledgeDict
        '''

        def subst_blank_chars_with_NA(string):
            '''
            Substitutes characters like ',' with "N/A"
            :param string:
            :return:
            '''

            if string is None:
                return "N/A"
            elif string in ["", "*", ","]:
                return "N/A"

            # Just return the normal string if it actually contains a value
            return string

        def YN_to_bool(string):
            '''
            Returns true or false depending on 'Yes' 'No' keywords
            :param string:
            :return:
            '''

            if string is None:
                return False
            elif string.lower() in ["yes", "true", "t", "y"]:
                return True
            return False

        def dollar_to_float(string):
            '''
            Filters out dollar sign and returns a float if string contains number, else returns 0
            :param string:
            :return: float
            '''

            # Return 0 if number was not specified
            if string is None:
                return 0

            # Get list version of string without numeric chars
            string = [i for i in string if i.isnumeric()]

            # Turns list back into string
            string = "".join(string)

            # If string didn't contain any numeric chars, return 0 dollars
            if string == "":
                return 0

            # Return float version of parsed number
            return float("".join(string))

        # Process strings
        pledge["firstName"] = subst_blank_chars_with_NA(pledge["firstName"])
        pledge["city"] = subst_blank_chars_with_NA(pledge["city"])

        # Parse amtDonated to float if exists, else default to 0$
        # TODO: See if this None comparison can be excluded since dollar_to_float() already does the comparison
        if pledge["amtDonated"] is None:
            pledge["amtDonated"] = 0
        else:
            pledge["amtDonated"] = dollar_to_float(pledge["amtDonated"])

        # If pledge is caller pledge, make pledgeType Caller, else website
        if pledge["pledgeType"] is None:
            pledge["pledgeType"] = 0
        elif pledge["pledgeType"].capitalize() == "Caller":
            pledge["pledgeType"] = 1
        else:
            pledge["pledgeType"] = 0

        # Process boolean values
        pledge["paidByCredit"] = YN_to_bool(pledge["paidByCredit"])
        pledge["isPaid"] = YN_to_bool(pledge["isPaid"])

        return pledge

    pledge = lex(row, head)
    pledge = parce(pledge)

    return pledge


def to_RadiothonInfo(donors=[], config={}):
    '''
    Given a list of ‘Donor’ data structures and a ‘serverConfig’ data structure,
    this method returns a ‘RadiothonInfo’ data structure.

    :param donors: PledgeDict
    :param config: ConfigDict
    :return: RadiothonInfoDict
    '''

    return \
    {
        'name': config["radiothon"]["name"],
        'startDate': config["radiothon"]["start_date"],
        'endDate': config["radiothon"]["end_date"],
        'goalHourly': config["radiothon"]["goal"]["hourly"],
        'goalDaily': config["radiothon"]["goal"]["daily"],
        'goalWeekly': config["radiothon"]["goal"]["weekly"],
        'goalTotal': config["radiothon"]["goal"]["total"],
        'pledges': donors
    }