import React from 'react';
import VacGraph from './VacGraph';

export default function VacRate(props) {



    return (
        <div className="panel">
            <div className="vac-rate">
            <h3>The current vaccination rate in {props.region} is</h3>
            <h1>XXX</h1>
            <p>This means that X out of 10 people in {props.region} have been vaccinated.</p>
            <VacGraph/>
            </div>
            
        </div>
    )
}
