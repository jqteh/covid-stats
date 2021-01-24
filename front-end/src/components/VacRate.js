import React from 'react';
import VacGraph from './VacGraph';

export default function VacRate(props) {

    // const data = [{"London":7539},{"South East": 3532},{"South West": 2563},
    // {"North East": 6342},{"East of England": 3112},{"Midlands": 9034},
    // {"East Midlands": 2123},{"West Midlands": 1233},{"Greater London": 9928},{"North West": 2343},]
    // var vacRate = 0;

    // data.forEach(obj => {
    //     if (obj.key === props.region) {
    //         vacRate = 
    //     }
    // })
    
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
