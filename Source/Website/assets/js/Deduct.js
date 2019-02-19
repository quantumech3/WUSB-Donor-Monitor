/*
Created by Scott Burgert on 2/19/2019
Project name: WUSB Donor Monitor

Module name: Deduct.js
Module description:
        Contains helpful methods used by many modules such as ‘Page.js’ to infer new radiothon information from what was given by server.
*/

/**
 * Returns true if date is a valid Date object else returns false.
 * @param date
 * @return {boolean}
 */
function isValidDate(date)
{
    try {
        // Return true if date obj is able to deduct a time from itself
        return !isNaN(date.getTime());
    }
    catch (e) {
        // Return false if date is not a Date object
        return false;
    }
}