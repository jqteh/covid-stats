import React from 'react'

export default function VacRate(props) {



    return (
        <div className="panel">
            <div className="vac-rate">
            <h3>The current vaccination rate is</h3>
            <h1>XXX</h1>
            <h3>in {props.region}.</h3>
            <p>This means that X/10 people in Cambridge have been vaccinated.</p>
            <p>insert graph here</p>
            </div>
            
        </div>
    )
}
