import React from 'react';
import HospitalLogo from '../assets/hospital.png';

export default function Hospital() {
    return (
        <div className="panel">
            <div className="hospital">
                <img src={HospitalLogo} alt=""/>
                <h3>The nearest hospital to you is</h3>
                <h1>Hospital X</h1>
                <h3>and it is running at X% capacity.</h3>
                <p>This means there might not be enough beds for you within this hospital. </p>
            </div>

        </div>
    )
}
