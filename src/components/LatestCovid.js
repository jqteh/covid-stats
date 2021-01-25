import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function LatestCovid(props) {

    const [newCases, setNewCases] = useState(null);
    const [newDeaths, setNewDeaths] = useState(null);
    const [isNull, setIsNull] = useState(false)


    useEffect(()=>{

        const bigRegions = ["London", "South East", "East of England", "South West", "West Midlands", "East Midlands","North East", "North West", "Yorkshire and The Humber"];

        var region = props.region;
        const london = ["Greater London"];
        if (london.includes(region)) {
            region = "London";
        }
    
    
        if (bigRegions.includes(region)===false) {
            region = "East of England";
            setIsNull(true);
        } else {
            setIsNull(false);
        }// Prevents API crashing if region not found

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
                AreaType = "region",
                AreaName = region;
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
        
            setNewCases(result["data"][1]["cases"]["new"]);
            setNewDeaths(result["data"][1]["deaths"]["new"]);
        
        };  // main
        latestCovid();
    },[props.region, newCases])



    return (
        <div className="latest-covid">
            <h3>New cases: {isNull ? "N/A" : newCases}</h3>
            <h3>New deaths: {isNull ? "N/A" : newDeaths}</h3>
        </div>
    )
}
