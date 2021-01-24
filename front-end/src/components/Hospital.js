import React from 'react';
import HospitalLogo from '../assets/hospital.png';
import bedOccupancy from '../critical_care_occupancy';

export default function Hospital(props) {

    var region = props.region;

    var occupied = bedOccupancy[0]["East of England"].slice(-1)[0].Occupied;
    var available = bedOccupancy[0]["East of England"].slice(-1)[0].Unoccupied;
    var capacity = Math.round((occupied - available)/occupied*100) + "%"

    const bigRegions = ["London", "South East", "East of England", "South West", "Midlands","North East", "North West"];
    const london = ["Greater London"];
    const midlands = ["East Midlands", "West Midlands"]
    const outside = ["Scotland", "Wales", "Non-geographic", "Channel Islands"]

    if (london.includes(region)) {
        region = "London"
    } else if (midlands.includes(region)) {
        region = "Midlands"
    }

    if (bigRegions.includes(region)) {
        occupied = bedOccupancy[0][region].slice(-1)[0].Occupied;
        available = bedOccupancy[0][region].slice(-1)[0].Unoccupied;
        capacity = Math.round((occupied - available)/occupied*100) + "%"
    } else {
        capacity = "N/A"
    }
    


    return (
        <div className="panel">
            <div className="hospital">
                <img src={HospitalLogo} alt=""/>
                <h3>Critical care services in {region} hospitals are running at</h3>
                <h1>{capacity}</h1>
                <h3>capacity.</h3>
                { capacity === "N/A" ? 
                (<p>Data for this region is not available.</p>) : 
                (<p>This means there might not be enough beds for you if you fall ill. </p>)
                }
            </div>
        </div>
    )
}
