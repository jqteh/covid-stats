import React, {useState} from 'react';
import HospitalLogo from '../assets/hospital.png';
import bedOccupancy from '../critical_care_occupancy';

export default function Hospital(props) {

    const [occupied, setOccupied] = useState(bedOccupancy[0].EastofEngland.slice(-1)[0].Occupied) // Default is East of England
    const [available, setAvailable] = useState(bedOccupancy[0].EastofEngland.slice(-1)[0].Unoccupied) // Default is East of England

    const capacity = Math.round((occupied - available)/occupied*100)


    return (
        <div className="panel">
            <div className="hospital">
                <img src={HospitalLogo} alt=""/>
                <h3>Critical care services in {props.region} hospitals are running at</h3>
                <h1>{capacity}%</h1>
                <h3>capacity.</h3>
                <p>This means there might not be enough beds for you if you fall ill. </p>
            </div>

        </div>
    )
}
