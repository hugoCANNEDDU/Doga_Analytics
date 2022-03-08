"use strict"

import * as scales from './scripts/scales.js'


(function (d3)  {
    let graphSize = {
        width : 1000,
        height : 600
    }

    let playground = d3.select("#playground")

    playground.attr("width", graphSize.width)
    .attr("height", graphSize.height)
    

    d3.csv('../data.csv').then((data) => {
        const colorScale = scales.setColorScale(data)
        const xScale = scales.setXScale(graphSize.width, data)
        const yScale = scales.setYScale(graphSize.height, data)
    })
})(d3)