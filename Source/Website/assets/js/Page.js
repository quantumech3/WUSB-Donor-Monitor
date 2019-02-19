/*
Created by Scott Burgert on 2/18/2019
Project name: WUSB Donor Monitor

Module name: Page.js
Module description:
        Contains static methods organized inside classes and used by inline JS to update what's shown on webpage.
        Updates elements in page using JQuery
*/

/**
 * Contains static methods for manipulating the red header on the top of the page
 */
class Header
{
    /**
     * Sets Radiothon name in header to value of title.
     * @string title
     * @returns void
     */
    static setRadiothonName(title="")
    {
        $('#title').text(title)
    }

    /**
     * Gets the name of the Radiothon currently being ran.
     * This information is gotten from the 'title' header at the top of the page
     * @returns string
     */
    static getRadiothonName()
    {
        return $('#title').text();
    }

    /**
     * Sets start date of Radiothon by setting the 'start_date' element to string form of param 'date'
     * @Date date
     * @returns void
     */
    static setStartDate(date=new Date())
    {
        if(isValidDate(date))
            // Set start date text in header to value of 'date'
            $('#start_date').text(date.toLocaleDateString());
        else
            console.error("Invalid object passed as 'date' parameter. Value passed: '" + date + "'");
    }

    /**
     * Gets start date of Radiothon in ‘start_date’
     * @return {Date}
     */
    static getStartDate()
    {
        let date = new Date($('#start_date').text());

        if(isValidDate(date))
            return date;
        // If 'start_date' value cannot be turned into Date type, throw an error.
        else
            console.error("Could not get value of 'start_date' as 'Date' type. Tried converting value: '" + $('#start_date').text() + "'");
    }

    /**
     * Sets text in ‘end_date’ to string representation of  of ‘date‘ and recalibrates ‘time_left‘ counter by setting the variable ‘_endDate’
     * @Date date
     * @return void
     */
    static setEndDate(date=new Date())
    {

        if(isValidDate(date))
        {
            // Set when ‘setEndDate()’ is called. Accessed when ‘getEndDate()’ is called, usually by inline JS for ‘time_left’ updates. Not meant to be accessed directly.
            Header._endDate = date;
            // Set end date text in header to value of 'date'
            $('#end_date').text(date.toLocaleDateString());
        }
        else
        {
            // Throw error if date is not a valid date object
            console.error("Invalid object passed as 'date' parameter. Value passed: '" + date + "'");
        }
    }

    /**
     * Returns end date of Radiothon if end date has been set, else returns 'Undefined'.
     * @return Date
     */
    static getEndDate()
    {
        // Returning internal variable instead of getting value from DOM because its faster when inline JS has to
        // constantly compare between the current time and the end date
        return Header._endDate;
    }
}

