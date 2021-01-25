import React from 'react';
import InfGraph from './InfGraph';

export default function InfRate(props) {

   const latestInf = props.infRate[Object.keys(props.infRate)[Object.keys(props.infRate).length-1]];

    return (
        <div className="panel">
            <div className="inf-rate">
                <h3>The following is a graph on the infection rate in {props.region}</h3>
                <InfGraph infRate={props.infRate}/>
                <p>The latest number of newly infected cases in {props.region} is {latestInf}.</p>
            </div>
        </div>
    )
}
