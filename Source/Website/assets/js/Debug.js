/*
Created by Scott Burgert on 2/19/2019
Project name: WUSB Donor Monitor

Module name: Debug.js
Module description:
        Contains methods used by virtually all the client-side modules used to throw errors and handle exceptions.
        Errors thrown are silenced when ‘DEBUG_MODE’ is set to false.
*/

/**
 * Website will log errors, warnings and debug messages if this value is set to true.
 * @type {boolean}
 */
DEBUG_MODE = true;

/**
 * Logs error text with value of “MONITOR_ERR[]: ‘msg’” if DEBUG_MODE is set to true.
 * @param msg
 */
function dbgErr(msg)
{
    if(DEBUG_MODE)
        console.error("MONITOR_ERR[]: " + msg)
}

/**
 * Logs warning text with value of “MONITOR_WARN[]: ‘msg’” if DEBUG_MODE is set to true.
 * @param msg
 */
function dbgWarn(msg)
{
    if(DEBUG_MODE)
        console.warn("MONITOR_WARN[]: " + msg)
}

/**
 * Logs error text with value of “MONITOR_DBG[]: ‘msg’” if DEBUG_MODE is set to true.
 * @param msg
 */
function dbgMsg(msg)
{
    if(DEBUG_MODE)
        console.log("MONITOR_DBG[]: " + msg)
}