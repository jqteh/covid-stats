import React from 'react';
import { ResponsiveLine } from '@nivo/line'

export default function VacGraph() {

    const data = [{
        "id": "japan",
        "color": "hsl(349, 70%, 50%)",
        "data": [
            {
                "x": "27/11",
                "y": 187
            },
            {
                "x": "3/12",
                "y": 192
            },
            {
                "x": "10/12",
                "y": 56
            },
            {
                "x": "17/12",
                "y": 166
            },
            {
                "x": "24/12",
                "y": 193
            },
            {
                "x": "31/12",
                "y": 160
            },
            {
                "x": "07/01",
                "y": 206
            },
            {
                "x": "14/01",
                "y": 175
            },
            {
                "x": "21/01",
                "y": 147
            }
        ]
    }]

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
