import React from 'react';
import VacGraph from './VacGraph';

export default function VacRate(props) {

    const currentVac = props.currentVac.toFixed(2) + "%";
    const herdDays = Math.round(props.herdDays);
    

    return (
        <div className="panel">
            <div className="vac-rate">
            <h3>Currently, the percentage of people vaccinated in {props.region} is</h3>
            <h1>{currentVac}</h1>
            <p>This means that {props.region} will achieve herd immunity in {herdDays} days</p>
            <VacGraph/>
            </div>
            
        </div>
    )
}
