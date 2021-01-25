import React from 'react';
import { ResponsiveLine } from '@nivo/line';

export default function InfGraph(props) {

    const infRate = props.infRate

    var dataPoints = [];

    for (const [key, value] of Object.entries(infRate)) {
        const dataPoint = {
            "x":key.substring(5,),
            "y":value
        };
        dataPoints.push(dataPoint);
      }

    const data = [{"data":dataPoints}]

    return (
        <div className="vac-graph">
            <ResponsiveLine
                data={data}
                margin={{ top: 18, right: 25, bottom: 30, left: 35 }}
                xScale={{ type: 'point' }}
                yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: true, reverse: false }}
                yFormat=" >-.2f"
                axisTop={null}
                axisRight={null}
                axisBottom={{
                    orient: 'bottom',
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    // legend: 'transportation',
                    legendOffset: 36,
                    legendPosition: 'middle'
                }}
                axisLeft={{
                    orient: 'left',
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'count',
                    legendOffset: -40,
                    legendPosition: 'middle'
                }}
                pointSize={10}
                pointColor={{ theme: 'background' }}
                pointBorderWidth={2}
                pointBorderColor={{ from: 'serieColor' }}
                pointLabelYOffset={-12}
                useMesh={true}
            />
        </div>
    )
}
