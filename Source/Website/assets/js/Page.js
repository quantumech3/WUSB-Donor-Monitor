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

/**
 * Contains methods for manipulating elements in the ‘Pledges’ tab
 */
class Pledges
{
    /**
     * Internal method used by setSomethingEntries() to edit table data.
     * This method takes in a list of data and returns HTML used for <table> entries
     * @list data
     * @return {string}
     * @private
     */
    static _toTableRow(data=[])
    {
        // htmlText accumulates html tags. Starts with <tr>
        let htmlText = "<tr>";

        // Add table column html code containing values from 'data[]'
        for(let i = 0; i < data.length; i++)
        {
            htmlText += "<td>" + data[i] + "</td>";
        }

        // Close htmlText with </tr>
        htmlText += "</tr>";

        return htmlText;
    }

    /**
     * Sets text in ‘credit_count‘ to value of ‘count’
     * @param count
     */
    static setCreditCount(count)
    {
        if(typeof count === 'number')
            $('#credit_count').text(count);
        else
            // Throw error if count is not a number
            console.error("Invalid object passed as 'count' parameter. Value passed: '" + count + "' should be a number");
    }

    /**
     * Gets value of ‘credit_count’ element
     * @return {number}
     */
    static getCreditCount()
    {
        // Gets text from credit_count element
        let count = $('#credit_count').text();

        // Attempt to parce credit_count text into float
        count = parseFloat(count);

        // Throw error if credit_count text cannot be casted to float
        if(isNaN(count))
            console.error("Could not cast credit_count value '" + $('#credit_count').text() + "' to float.");
        else
            return count;
    }

    /**
     * Sets text in ‘credit_total‘ to value of ‘total’
     * @float total
     */
    static setCreditTotal(total)
    {
        if(typeof total === 'number')
            $('#credit_total').text(total);
        else
            // Throw error if total is not a number
            console.error("Invalid object passed as 'total' parameter. Value passed: '" + total + "' should be a number");
    }

    /**
     * Gets the current credit total by getting text from element ‘credit_total’ as float.
     * @return {number}
     */
    static getCreditTotal()
    {
        // Gets text from credit_total element
        let total = $('#credit_total').text();

        // Attempt to parce credit_total text into float
        total = parseFloat(total);

        // Throw error if credit_total text cannot be casted to float
        if(isNaN(total))
            console.error("Could not cast credit_total value '" + $('#credit_total').text() + "' to float.");
        else
            return total;
    }

    /**
     * ‘entries’ contain ‘Pledge‘ structures.
     *  Sets the values inside ‘credit_list‘ to ‘entries’.
     *  Specifically, it displays the ‘firstName’, ‘city’ and ‘amtDonated’ parts from each element of ‘entries’.
     * @PledgeEnum[] entries
     */
    static setCreditEntries(entries=[])
    {
        // Accumulating html and setting all at once instead of appending 1 after another to avoid weird visual during updates.
        let tblHtml = "";

        // Add html containing columns with value of all donor's first name, city and amount donated
        for(let i = 0; i < entries.length; i++)
        {
            if(typeof entries[i].firstName !== "string") // Throw error if donor.firstName is not a string
                console.error("entries[" + i + "].firstName with value '" + entries[i].firstName + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].city !== "string") // Throw error if donor.city is not a string
                console.error("entries[" + i + "].city with value '" + entries[i].city + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].amtDonated !== "number") // Throw error if donor.amtDonated is not a float
                console.error("entries[" + i + "].amtDonated with value '" + entries[i].amtDonated + "' is supposed to be 'float' type but isnt");
            else
                // Add table row containing [donor.firstName, donor.city, '$' + donor.amtDonated] to tblHtml
                tblHtml += Pledges._toTableRow([entries[i].firstName, entries[i].city, '$' + entries[i].amtDonated]);
        }

        // Update credit_list to display tblHtml rows and columns
        $("#credit_list").html(tblHtml);
    }

    /**
     * Sets current credit donors being displayed to values inside entries. Updates credit total, count,
     * and entries in table
     * @PledgeEnum[] entries
     */
    static updateCreditView(entries=[])
    {
        let total = totalDonated(entries);

        Pledges.setCreditEntries(entries);
        Pledges.setCreditTotal(total);
        Pledges.setCreditCount(entries.length);
    }

    /**
     * Sets text in ‘web_count‘ to value of ‘count’
     * @param count
     */
    static setWebCount(count)
    {
        if(typeof count === 'number')
            $('#web_count').text(count);
        else
            // Throw error if count is not a number
            console.error("Invalid object passed as 'count' parameter. Value passed: '" + count + "' should be a number");
    }

    /**
     * Gets value of ‘web_count’ element
     * @return {number}
     */
    static getWebCount()
    {
        // Gets text from web_count element
        let count = $('#web_count').text();

        // Attempt to parce web_count text into float
        count = parseFloat(count);

        // Throw error if web_count text cannot be casted to float
        if(isNaN(count))
            console.error("Could not cast web_count value '" + $('#web_count').text() + "' to float.");
        else
            return count;
    }

    /**
     * Sets text in ‘web_total‘ to value of ‘total’
     * @float total
     */
    static setWebTotal(total)
    {
        if(typeof total === 'number')
            $('#web_total').text(total);
        else
        // Throw error if total is not a number
            console.error("Invalid object passed as 'total' parameter. Value passed: '" + total + "' should be a number");
    }

    /**
     * Gets the current web total by getting text from element ‘web_total’ as float.
     * @return {number}
     */
    static getWebTotal()
    {
        // Gets text from web_total element
        let total = $('#web_total').text();

        // Attempt to parce web_total text into float
        total = parseFloat(total);

        // Throw error if web_total text cannot be casted to float
        if(isNaN(total))
            console.error("Could not cast web_total value '" + $('#web_total').text() + "' to float.");
        else
            return total;
    }

    /**
     * ‘entries’ contain ‘Pledge‘ structures.
     *  Sets the values inside ‘web_list‘ to ‘entries’.
     *  Specifically, it displays the ‘firstName’, ‘city’ and ‘amtDonated’ parts from each element of ‘entries’.
     * @PledgeEnum[] entries
     */
    static setWebEntries(entries=[])
    {
        // Accumulating html and setting all at once instead of appending 1 after another to avoid weird visual during updates.
        let tblHtml = "";

        // Add html containing columns with value of all donor's first name, city and amount donated
        for(let i = 0; i < entries.length; i++)
        {
            if(typeof entries[i].firstName !== "string") // Throw error if donor.firstName is not a string
                console.error("entries[" + i + "].firstName with value '" + entries[i].firstName + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].city !== "string") // Throw error if donor.city is not a string
                console.error("entries[" + i + "].city with value '" + entries[i].city + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].amtDonated !== "number") // Throw error if donor.amtDonated is not a float
                console.error("entries[" + i + "].amtDonated with value '" + entries[i].amtDonated + "' is supposed to be 'float' type but isnt");
            else
            // Add table row containing [donor.firstName, donor.city, '$' + donor.amtDonated] to tblHtml
                tblHtml += Pledges._toTableRow([entries[i].firstName, entries[i].city, '$' + entries[i].amtDonated]);
        }

        // Update web_list to display tblHtml rows and columns
        $("#web_list").html(tblHtml);
    }

    /**
     * Sets current web donors being displayed to values inside entries. Updates web total, count,
     * and entries in table
     * @PledgeEnum[] entries
     */
    static updateWebView(entries=[])
    {
        let total = totalDonated(entries);

        Pledges.setWebEntries(entries);
        Pledges.setWebTotal(total);
        Pledges.setWebCount(entries.length);
    }

    /**
     * Sets text in ‘paid_count‘ to value of ‘count’. Sets the amount of paid caller entries there are.
     * @param count
     */
    static setPaidCount(count)
    {
        if(typeof count === 'number')
            $('#paid_count').text(count);
        else
            // Throw error if count is not a number
            console.error("Invalid object passed as 'count' parameter. Value passed: '" + count + "' should be a number");
    }

    /**
     * Gets value of ‘paid_count’ element. Gets how many 'paid caller' entries there are.
     * @return {number}
     */
    static getPaidCount()
    {
        // Gets text from paid_count element
        let count = $('#paid_count').text();

        // Attempt to parce paid_count text into float
        count = parseFloat(count);

        // Throw error if paid_count text cannot be casted to float
        if(isNaN(count))
            console.error("Could not cast paid_count value '" + $('#paid_count').text() + "' to float.");
        else
            return count;
    }

    /**
     * Sets text in ‘paid_caller_total‘ to value of ‘total’
     * @float total
     */
    static setPaidTotal(total)
    {
        if(typeof total === 'number')
            $('#paid_caller_total').text(total);
        else
            // Throw error if total is not a number
            console.error("Invalid object passed as 'total' parameter. Value passed: '" + total + "' should be a number");
    }

    /**
     * Gets the current paid caller total by getting text from element ‘paid_caller_total’ as float.
     * @return {number}
     */
    static getPaidTotal()
    {
        // Gets text from paid_caller_total element
        let total = $('#paid_caller_total').text();

        // Attempt to parce paid_caller_total text into float
        total = parseFloat(total);

        // Throw error if paid_caller_total text cannot be casted to float
        if(isNaN(total))
            console.error("Could not cast paid_caller_total value '" + $('#paid_caller_total').text() + "' to float.");
        else
            return total;
    }

    /**
     * ‘entries’ contain ‘Pledge‘ structures.
     *  Sets the values inside ‘paid_list‘ to ‘entries’.
     *  Specifically, it displays the ‘firstName’, ‘city’ and ‘amtDonated’ parts from each element of ‘entries’.
     * @PledgeEnum[] entries
     */
    static setPaidEntries(entries=[])
    {
        // Accumulating html and setting all at once instead of appending 1 after another to avoid weird visual during updates.
        let tblHtml = "";

        // Add html containing columns with value of all donor's first name, city and amount donated
        for(let i = 0; i < entries.length; i++)
        {
            if(typeof entries[i].firstName !== "string") // Throw error if donor.firstName is not a string
                console.error("entries[" + i + "].firstName with value '" + entries[i].firstName + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].city !== "string") // Throw error if donor.city is not a string
                console.error("entries[" + i + "].city with value '" + entries[i].city + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].amtDonated !== "number") // Throw error if donor.amtDonated is not a float
                console.error("entries[" + i + "].amtDonated with value '" + entries[i].amtDonated + "' is supposed to be 'float' type but isnt");
            else
            // Add table row containing [donor.firstName, donor.city, '$' + donor.amtDonated] to tblHtml
                tblHtml += Pledges._toTableRow([entries[i].firstName, entries[i].city, '$' + entries[i].amtDonated]);
        }

        // Update paid_list to display tblHtml rows and columns
        $("#paid_list").html(tblHtml);
    }

    /**
     * Sets current paid caller donors being displayed to values inside entries. Updates paid caller total, count,
     * and entries in table
     * @PledgeEnum[] entries
     */
    static updatePaidView(entries=[])
    {
        let total = totalDonated(entries);

        Pledges.setPaidEntries(entries);
        Pledges.setPaidTotal(total);
        Pledges.setPaidCount(entries.length);
    }

    /**
     * Sets text in ‘unpaid_count‘ to value of ‘count’. Sets the amount of unpaid caller entries there are.
     * @param count
     */
    static setUnpaidCount(count)
    {
        if(typeof count === 'number')
            $('#unpaid_count').text(count);
        else
            // Throw error if count is not a number
            console.error("Invalid object passed as 'count' parameter. Value passed: '" + count + "' should be a number");
    }

    /**
     * Gets value of ‘unpaid_count’ element. Gets how many 'unpaid caller' entries there are.
     * @return {number}
     */
    static getUnpaidCount()
    {
        // Gets text from unpaid_count element
        let count = $('#unpaid_count').text();

        // Attempt to parce unpaid_count text into float
        count = parseFloat(count);

        // Throw error if paid_count text cannot be casted to float
        if(isNaN(count))
            console.error("Could not cast unpaid_count value '" + $('#unpaid_count').text() + "' to float.");
        else
            return count;
    }

    /**
     * Sets text in ‘unpaid_caller_total‘ to value of ‘total’
     * @float total
     */
    static setUnpaidTotal(total)
    {
        if(typeof total === 'number')
            $('#unpaid_caller_total').text(total);
        else
            // Throw error if total is not a number
            console.error("Invalid object passed as 'total' parameter. Value passed: '" + total + "' should be a number");
    }

    /**
     * Gets the current unpaid caller total by getting text from element ‘unpaid_caller_total’ as float.
     * @return {number}
     */
    static getUnpaidTotal()
    {
        // Gets text from unpaid_caller_total element
        let total = $('#unpaid_caller_total').text();

        // Attempt to parce unpaid_caller_total text into float
        total = parseFloat(total);

        // Throw error if unpaid_caller_total text cannot be casted to float
        if(isNaN(total))
            console.error("Could not cast unpaid_caller_total value '" + $('#unpaid_caller_total').text() + "' to float.");
        else
            return total;
    }

    /**
     * ‘entries’ contain ‘Pledge‘ structures.
     *  Sets the values inside ‘unpaid_list‘ to ‘entries’.
     *  Specifically, it displays the ‘firstName’, ‘city’ and ‘amtDonated’ parts from each element of ‘entries’.
     * @PledgeEnum[] entries
     */
    static setUnpaidEntries(entries=[])
    {
        // Accumulating html and setting all at once instead of appending 1 after another to avoid weird visual during updates.
        let tblHtml = "";

        // Add html containing columns with value of all donor's first name, city and amount donated
        for(let i = 0; i < entries.length; i++)
        {
            if(typeof entries[i].firstName !== "string") // Throw error if donor.firstName is not a string
                console.error("entries[" + i + "].firstName with value '" + entries[i].firstName + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].city !== "string") // Throw error if donor.city is not a string
                console.error("entries[" + i + "].city with value '" + entries[i].city + "' is supposed to be 'string' type but isnt");
            else if(typeof entries[i].amtDonated !== "number") // Throw error if donor.amtDonated is not a float
                console.error("entries[" + i + "].amtDonated with value '" + entries[i].amtDonated + "' is supposed to be 'float' type but isnt");
            else
            // Add table row containing [donor.firstName, donor.city, '$' + donor.amtDonated] to tblHtml
                tblHtml += Pledges._toTableRow([entries[i].firstName, entries[i].city, '$' + entries[i].amtDonated]);
        }

        // Update unpaid_list to display tblHtml rows and columns
        $("#unpaid_list").html(tblHtml);
    }

    /**
     * Sets current unpaid caller donors being displayed to values inside entries. Updates unpaid caller total, count,
     * and entries in table
     * @PledgeEnum[] entries
     */
    static updateUnpaidView(entries=[])
    {
        let total = totalDonated(entries);

        Pledges.setUnpaidEntries(entries);
        Pledges.setUnpaidTotal(total);
        Pledges.setUnpaidCount(entries.length);
    }
}

class RecentDonor
{
    /**
     * Sets element ‘recent_name’ to ‘name’
     * @string name
     */
    static setName(name)
    {
        $('#recent_name').text(name);
    }

    /**
     * Gets value of element ‘recent_name‘
     * @return {string}
     */
    static getName()
    {
        return $('#recent_name').text();
    }

    /**
     * Sets element ‘recent_amt’ to value of ‘amt’ plus a ‘$’ character
     * @float amt
     */
    static setAmtDonated(amt)
    {
        if(typeof amt === 'number')
            $('#recent_amt').text('$' + amt.toString());
        else
            console.error("Parameter 'amt' with value '" + amt + "' is supposed to be type 'float' but isn't");
    }

    /**
     * Gets value of element ‘recent_amt‘ minus the ‘$’ character
     * @return {number}
     */
    static getAmtDonated()
    {
        // Get text from 'recent_amt' element
        let num = $('#recent_amt').text();

        // Chop off '$' at beginning of string
        if(num[0] == '$')
            num = num.substr(1);

        // Attempt to convert 'recent_amt' text to float
        num = parseFloat(num);

        // Throw error if 'recent_amt' text could not be converted to float
        if(isNaN(num))
            console.error("Could not cast recent_amt value '" + $('#recent_amt').text() + "' to float.");
        else
            return num;
    }

    /**
     * Sets the most recent donor and displays it on the page.
     * @PledgeEnum donor
     */
    static setDonor(donor)
    {
        if(typeof donor.firstName === 'string')
            RecentDonor.setName(donor.firstName);
        else
            // Throw error if donor.firstName is not of type 'string'
            console.error("donor.firstName with value '" + donor.firstName + "' is supposed to be type 'string' but isnt");

        if(typeof donor.amtDonated === 'number')
            RecentDonor.setAmtDonated(donor.amtDonated);
        else
            // Throw error if donor.firstName is not of type 'number'
            console.error("donor.amtDonated with value '" + donor.amtDonated + "' is supposed to be type 'number' but isnt");
    }
}

/**
 * Contains methods for setting and getting the ‘paid_total‘ and ‘full_total’ HTML elements
 */
class Totals
{
    /**
     * This sets the ‘paid_total’ HTML element to the sum of all the donors[n].amtDonated values
     * @PledgeEnum[] donors
     */
    static setPaidTotal(donors=[])
    {
        // Setting float precision to prevent astronomically large numbers (which would not look good on a webpage)
        $('#paid_total').text('$' + totalDonated(donors).toPrecision(10));
    }

    /**
     * This gets the value of ‘paid_total’ HTML element
     * @return {number}
     */
    static getPaidTotal()
    {
        // Get text from 'paid_total' element
        let total = $('#paid_total').text();

        // Get rid of '$' at beginning of string
        if(total[0] === '$')
            total = total.substr(1);

        // Attempt to cast 'total' to number
        total = parseFloat(total);

        // Throw error if 'total' is non-numeric
        if(isNaN(total))
            console.error("Cannot convert value from paid_total '" + $('#paid_total').text() + "' to number.");
        else
            return total;
    }

    /**
     * This sets the ‘full_total’ HTML element to the sum of all the donors[n].amtDonated values with a ‘$’ at the beginning
     * @PledgeEnum[] donors
     */
    static setFullTotal(donors)
    {
        // Setting float precision to prevent astronomically large numbers (which would not look good on a webpage)
        $('#full_total').text('$' + totalDonated(donors).toPrecision(10));
    }

    /**
     * This gets the value of ‘full_total’ HTML element
     * @return {number}
     */
    static getFullTotal()
    {
        // Get text from 'full_total' element
        let total = $('#full_total').text();

        // Get rid of '$' at beginning of string
        if(total[0] === '$')
            total = total.substr(1);

        // Attempt to cast 'total' to number
        total = parseFloat(total);

        // Throw error if 'total' is non-numeric
        if(isNaN(total))
            console.error("Cannot convert value from full_total '" + $('#full_total').text() + "' to number.");
        else
            return total;
    }
}