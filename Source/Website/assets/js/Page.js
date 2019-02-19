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

/**
 * Contains methods for manipulating elements in the ‘Goals’ tab
 */
class Goals
{
    /**
     * Sets ‘goal_hourly’ element to string version of ‘goal’ with a ‘$’ at the beginning
     * @number goal
     * @return void
     */
    static setHourly(goal=0.0)
    {
        if (typeof goal === "number")
            $('#goal_hourly').text('$' + goal.toString());
        else
            // Throw error if goal is not a number
            console.error("Invalid object passed as 'goal' parameter. Value passed: '" + goal + "' should be a number");
    }

    /**
     * Extrapolates value of ‘goal_hourly’ element without ‘$’ character
     * @return {number}
     */
    static getHourly()
    {
        // Get text from 'goal_hourly' element
        let num = $('#goal_hourly').text();

        // Chop off '$' at beginning of string
        if(num[0] == '$')
            num = num.substr(1);

        // Attempt to convert goal_hourly text to float
        num = parseFloat(num);

        // Throw error if goal_hourly text could not be converted to float
        if(isNaN(num))
            console.error("Could not cast goal_hourly value '" + $('#goal_hourly').text() + "' to float.");
        else
            return num;
    }

    /**
     * Sets ‘goal_daily’ element to string version of ‘goal’ with a ‘$’ at the beginning
     * @number goal
     */
    static setDaily(goal=0.0)
    {
        if (typeof goal === "number")
            $('#goal_daily').text('$' + goal.toString());
        else
            // Throw error if goal is not a number
            console.error("Invalid object passed as 'goal' parameter. Value passed: '" + goal + "' should be a number");
    }

    /**
     * Extrapolates value of ‘goal_daily’ element without ‘$’ character
     * @return {number}
     */
    static getDaily()
    {
        // Get text from 'goal_daily' element
        let num = $('#goal_daily').text();

        // Chop off '$' at beginning of string
        if(num[0] == '$')
            num = num.substr(1);

        // Attempt to convert goal_daily text to float
        num = parseFloat(num);

        // Throw error if goal_daily text could not be converted to float
        if(isNaN(num))
            console.error("Could not cast goal_daily value '" + $('#goal_daily').text() + "' to float.");
        else
            return num;
    }

    /**
     * Sets ‘goal_weekly’ element to string version of ‘goal’ with a ‘$’ at the beginning
     * @number goal
     */
    static setWeekly(goal=0.0)
    {
        if (typeof goal === "number")
            $('#goal_weekly').text('$' + goal.toString());
        else
            // Throw error if goal is not a number
            console.error("Invalid object passed as 'goal' parameter. Value passed: '" + goal + "' should be a number");
    }

    /**
     * Extrapolates value of ‘goal_weekly’ element without ‘$’ character
     * @return {number}
     */
    static getWeekly()
    {
        // Get text from 'goal_weekly' element
        let num = $('#goal_weekly').text();

        // Chop off '$' at beginning of string
        if(num[0] == '$')
            num = num.substr(1);

        // Attempt to convert goal_weekly text to float
        num = parseFloat(num);

        // Throw error if goal_weekly text could not be converted to float
        if(isNaN(num))
            console.error("Could not cast goal_weekly value '" + $('#goal_weekly').text() + "' to float.");
        else
            return num;
    }

    /**
     * Sets ‘goal_total’ element to string version of ‘goal’ with a ‘$’ at the beginning
     * @number goal
     */
    static setTotal(goal=0.0)
    {
        if (typeof goal === "number")
            $('#goal_total').text('$' + goal.toString());
        else
            // Throw error if goal is not a number
            console.error("Invalid object passed as 'goal' parameter. Value passed: '" + goal + "' should be a number");
    }

    /**
     * Extrapolates value of ‘goal_total’ element without ‘$’ character
     * @return {number}
     */
    static getTotal()
    {
        // Get text from 'goal_total' element
        let num = $('#goal_total').text();

        // Chop off '$' at beginning of string
        if(num[0] == '$')
            num = num.substr(1);

        // Attempt to convert goal_total text to float
        num = parseFloat(num);

        // Throw error if goal_total text could not be converted to float
        if(isNaN(num))
            console.error("Could not cast goal_total value '" + $('#goal_total').text() + "' to float.");
        else
            return num;
    }
}

