import React from 'react';
import VacGraph from './VacGraph';

export default function InfRate(props) {
    return (
        <div className="panel">
            <div className="inf-rate">
                <h3>The virus is becoming more infectious, the following is a graph on the infection rate in {props.region}</h3>
                <VacGraph/>
                <p>Your risk of being infected with Covid-19 in {props.region} is 46%.</p>
            </div>
        </div>
    )
}