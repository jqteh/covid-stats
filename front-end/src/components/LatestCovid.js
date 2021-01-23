import React, {useState, useEffect} from 'react'
import axios from 'axios';

export default function LatestCovid() {

    const getData = async ( queries ) => {
        const endpoint = 'https://api.coronavirus.data.gov.uk/v1/data';
        const { data, status, statusText } = await axios.get(endpoint, { 
            params: queries,
            timeout: 10000 
        });
        if ( status >= 400 )
            throw new Error(statusText);
        return data
    };  // getData
    
    
    const latestCovid = async () => {
        const
            AreaType = "nation",
            AreaName = "england";
        const
            filters = [
                `areaType=${ AreaType }`,
                `areaName=${ AreaName }`
            ],
            structure = {
                date: "date",
                name: "areaName",
                code: "areaCode",
                cases: {
                    new: "newCasesByPublishDate",
                    cumulative: "cumCasesByPublishDate"
                },
                deaths: {
                    new: "newDeathsByDeathDate",
                    cumulative: "cumDeathsByDeathDate"
                }
            };
        const
            apiParams = {
                filters: filters.join(";"),
                structure: JSON.stringify(structure),
            };
    
        const result = await getData(apiParams);
    
        const latestResult = result["data"][1];
    
        console.log(JSON.stringify(latestResult));
    
    };  // main

    return (
        <div>
            <button onClick={latestCovid}>Fetch</button>

        </div>
    )
}
