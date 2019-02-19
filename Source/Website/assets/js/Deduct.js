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

/**
 * Extrapolates and returns an array of all ‘Pledge’ structures with ‘paidByCredit’ set to true
 * @DonorEnum[] donors
 * @return DonorEnum[]
 */
function extpCreditDonors(donors=[])
{
    // Accumulates all Donor objects in 'donors' with 'paidByCredit' set to true
    let creditDonors = [];

    // Aggregate through donors and append all donors to 'creditDonors' with 'paidByCredit' = true
    for(let i = 0; i < donors.length; i++)
    {
        // Throw error if donor.paidByCredit is not a boolean
        if(typeof donors[i].paidByCredit !== 'boolean')
            console.error("Invalid '" + donors[i].paidByCredit + "' passed into donors[" + i + "].paidByCredit. Donor.paidByCredit should be Boolean");
        // Append donors[i] to creditDonors if donors[i].paidByCredit = true
        else if(donors[i].paidByCredit)
            creditDonors.push(donors[i])
    }

    return creditDonors;
}

/**
 * Extrapolates and returns an array of all ‘Pledge’ structures with ‘pledgeType' set to 0
 * @DonorEnum[] donors
 * @return DonorEnum[]
 */
function extpWebDonors(donors=[])
{
    // Accumulates all Donor objects in 'donors' with 'pledgeType' set to 0
    let webDonors = [];

    // Aggregate through donors and append all donors to 'webDonors' with 'pledgeType' set to 0
    for(let i = 0; i < donors.length; i++)
    {
        // Throw error if donor.pledgeType is not a number
        if(typeof donors[i].pledgeType !== 'number')
            console.error("Invalid '" + donors[i].pledgeType + "' passed into donors[" + i + "].pledgeType. Donor.pledgeType should be number");
        // Append donors[i] to webDonors if donors[i] paid via website
        else if(donors[i].pledgeType === 0)
            webDonors.push(donors[i])
    }

    return webDonors;
}

/**
 * Extrapolates and returns an array of all ‘Pledge’ structures with ‘pledgeType' set to 1
 * @DonorEnum[] donors
 * @return DonorEnum[]
 */
function extpCallDonors(donors=[])
{
    // Accumulates all Donor objects in 'donors' with 'pledgeType' set to 1
    let callDonors = [];

    // Aggregate through donors and append all donors to 'callDonors' with 'pledgeType' set to 1
    for(let i = 0; i < donors.length; i++)
    {
        // Throw error if donor.pledgeType is not a number
        if(typeof donors[i].pledgeType !== 'number')
            console.error("Invalid '" + donors[i].pledgeType + "' passed into donors[" + i + "].pledgeType. Donor.pledgeType should be number");
        // Append donors[i] to callDonors if donors[i] paid via call
        else if(donors[i].pledgeType === 1)
            callDonors.push(donors[i])
    }

    return callDonors;
}

/**
 * Extrapolates and returns an array of all ‘Pledge’ structures with ‘isPaid’ set to true
 * @DonorEnum[] donors
 * @return DonorEnum[]
 */
function extpPaidDonors(donors=[])
{
    // Accumulates all Donor objects in 'donors' with 'isPaid' set to true
    let paidDonors = [];

    // Aggregate through donors and append all donors to 'paidDonors' with 'isPaid' set to true
    for(let i = 0; i < donors.length; i++)
    {
        // Throw error if donor.isPaid is not a boolean
        if(typeof donors[i].isPaid !== 'boolean')
            console.error("Invalid '" + donors[i].isPaid + "' passed into donors[" + i + "].isPaid. Donor.isPaid should be boolean");
        // Append donors[i] to paidDonors if donors[i] paid
        else if(donors[i].isPaid)
            paidDonors.push(donors[i])
    }

    return paidDonors;
}

/**
 * Extrapolates and returns an array of all ‘Pledge’ structures with ‘isPaid’ set to false
 * @DonorEnum[] donors
 * @return DonorEnum[]
 */
function extpUnpaidDonors(donors=[])
{
    // Accumulates all Donor objects in 'donors' with 'isPaid' set to false
    let unpaidDonors = [];

    // Aggregate through donors and append all donors to 'unpaidDonors' with 'isPaid' set to false
    for(let i = 0; i < donors.length; i++)
    {
        // Throw error if donor.isPaid is not a boolean
        if(typeof donors[i].isPaid !== 'boolean')
            console.error("Invalid '" + donors[i].isPaid + "' passed into donors[" + i + "].isPaid. Donor.isPaid should be boolean");
        // Append donors[i] to unpaidDonors if donors[i] didn't pay
        else if(!donors[i].isPaid)
            unpaidDonors.push(donors[i])
    }

    return unpaidDonors;
}

/**
 * Returns the sum of all of ‘donors’s ‘amtDonated’ values
 * @DonorEnum[] donors
 * @return {number}
 */
function totalDonated(donors=[])
{
    let total = 0;

    // Add all donors[i] to total
    for(let i = 0; i < donors.length; i++)
    {
        // If donors[i].amtDonated is a number, add to total
        if(typeof donors[i].amtDonated === 'number')
            total += donors[i].amtDonated;
        // If donors[i].amtDonated is not a number, throw an error
        else
            console.error("Invalid '" + donors[i].amtDonated + "' passed into donors[" + i + "].amtDonated. Donor.amtDonated should be number");
    }

    return total
}