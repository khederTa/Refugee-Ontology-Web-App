// const nodes1 = [
//     { "name": "PHDStudent",       "description": "description" },
//     { "name": "Samer1",           "description": "description" },
//     { "name": "PHD",              "description": "description" },
//     { "name": "TestAgencyQuery2", "description": "description" },
//     { "name": "TestAgencyQuery1", "description": "description" },
//     { "name": "Samer3",           "description": "description" },
//     { "name": "Poor",             "description": "description" }
// ];

// const edges1 = [
//     { "source": "PHDStudent",       "target": "Samer1", "relationship": "Label" },
//     { "source": "Samer1",           "target": "PHD",    "relationship": "Label" },
//     { "source": "TestAgencyQuery2", "target": "PHD",    "relationship": "Label" },
//     { "source": "TestAgencyQuery1", "target": "PHD",    "relationship": "Label" },
//     { "source": "Samer3",           "target": "Poor",   "relationship": "Label" }
// ];

// const nodes2 = [
//     { "name": "NamedIndividual", "description": "description" },
//     { "name": "Samer1",          "description": "description" },
//     { "name": "Refugee",         "description": "description" }
// ];

// const edges2 = [
//     { "source": "Samer1", "target": "NamedIndividual", "relationship": "Label" },
//     { "source": "Samer1", "target": "Refugee",         "relationship": "Label" }
// ];

// const nodes3 = [
//     { "name": "HighAgency",       "description": "description" },
//     { "name": "TestAgencyQuery2", "description": "description" },
//     { "name": "Samer1",           "description": "description" },
//     { "name": "PHD",              "description": "description" },
//     { "name": "PHDStudent",       "description": "description" }
// ];

// const edges3 = [
//     { "source": "TestAgencyQuery2", "target": "PHD", "relationship": "HasAgency" },
//     { "source": "PHD",              "target": "HighAgency", "relationship": "Label" },
//     { "source": "PHDStudent",       "target": "HighAgency", "relationship": "Label" },
//     { "source": "Samer1",           "target": "PHD", "relationship": "HasAgency" },
//     { "source": "Samer1",           "target": "PHDStudent", "relationship": "HasAgency" }
// ];

// const nodes4 = [
//     { "name": "IllegalRefugee", "description": "description" },
//     { "name": "LegalRefugee",   "description": "description" },
//     { "name": "Refugee",        "description": "description" },
//     { "name": "Nationalized",   "description": "description" },
//     { "name": "Stayee",         "description": "description" }
// ];

// const edges4 = [
//     { "source": "IllegalRefugee", "target": "Refugee", "relationship": "Label" },
//     { "source": "LegalRefugee",   "target": "Refugee", "relationship": "Label" },
//     { "source": "Nationalized",   "target": "Refugee", "relationship": "Label" },
//     { "source": "Stayee",         "target": "Refugee", "relationship": "Unknwon" }
// ];


// const nodes5 = [
//     { "name": "NamedIndividual",    "description": "description" },
//     { "name": "TestAgencyQuery1",   "description": "description" },
//     { "name": "WouldBeReturnee",    "description": "description" },
//     { "name": "PHD", "description": "description" }
// ];

// const edges5 = [
//     { "source": "TestAgencyQuery1", "target": "NamedIndividual", "relationship": "Label" },
//     { "source": "TestAgencyQuery1", "target": "WouldBeReturnee", "relationship": "Label" },
//     { "source": "TestAgencyQuery1", "target": "PHD",             "relationship": "HasAgency" }
// ];

const nodes6 = [
    {"name": "WouldBeReturnee",   "description": "",  "color": "#555"},
    {"name": "Samer1",            "description": "",  "color": "#AAA"},
    {"name": "Samer2",            "description": "",  "color": "#AAA"},
    {"name": "Samer3",            "description": "",  "color": "#AAA"},
    {"name": "PHD",               "description": "",  "color": "#AAA"},
    {"name": "Remittance",        "description": "",  "color": "#AAA"},
    {"name": "Friends",           "description": "",  "color": "#AAA"},
    {"name": "CastleInSyria",     "description": "",  "color": "#AAA"},
    {"name": "Poor",              "description": "",  "color": "#AAA"},
    {"name": "HighAgency",        "description": "",  "color": "#555"},
    {"name": "Transnationalism",  "description": "",  "color": "#555"},
    {"name": "HomeBelonging",     "description": "",  "color": "#555"},
    {"name": "HomeAttachment",    "description": "",  "color": "#555"},
    {"name": "LowAgency",         "description": "",  "color": "#555"},
]
const edges6 = [
    {"source":"WouldBeReturnee"    , "target": "Samer1"         , "relationship": ""},
    {"source":"WouldBeReturnee"    , "target": "Samer2"         , "relationship": ""},
    {"source":"WouldBeReturnee"    , "target": "Samer3"         , "relationship": ""},
    {"source":"Samer1"             , "target": "PHD"            , "relationship": ""},
    {"source":"Samer1"             , "target": "Remittance"     , "relationship": ""},
    {"source":"Samer2"             , "target": "Friends"        , "relationship": ""},
    {"source":"Samer3"             , "target": "CastleInSyria"  , "relationship": ""},
    {"source":"Samer3"             , "target": "Poor"           , "relationship": ""},
    {"source":"HighAgency"         , "target": "PHD"            , "relationship": ""},
    {"source":"Transnationalism"   , "target": "Remittance"     , "relationship": ""},
    {"source":"HomeBelonging"      , "target": "Friends"        , "relationship": ""},
    {"source":"HomeAttachment"     , "target": "CastleInSyria"  , "relationship": ""},
    {"source":"LowAgency"          , "target": "Poor"           , "relationship": ""}
]
go(nodes6, edges6)
// function query1() {
//     go(nodes1, edges1);
// }
// function query2() {
//     go(nodes2, edges2);
// }
// function query3() {
//     go(nodes3, edges3);
// }
// function query4() {
//     go(nodes4, edges4);
// }
// function query5() {
//     go(nodes5, edges5);
// }

function go(nodes0, edges0) {
    var svg_query = d3.select("#svg_query");
    svg_query.selectAll("*").remove();
    const width_query = +svg_query.attr("width");
    const height_query = +svg_query.attr("height");

    // Create the simulation with the desired forces
    const simulation_query = d3.forceSimulation(nodes0)
        .force("link", d3.forceLink(edges0).id(d => d.name))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width_query / 2, height_query / 2));

    // Create the links and add them to the SVG
    const link_query = svg_query.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(edges0)
        .enter().append("line")
        .attr("stroke-width", 1)
        .attr("stroke", "#999")
        .attr("marker-end", "url(#arrowhead)");

    // Create the nodes1 and add them to the SVG
    const node_query = svg_query.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(nodes0)
        .enter().append("circle")
        .attr("r", 10)
        .attr("fill", d=>d.color)
        .attr("stroke", "#fff")
        .attr("stroke-width", 2)
        .call(d3.drag()
            .on("start", dragstarted_query)
            .on("drag", dragged_query)
            .on("end", dragended_query))
        // .on("click", click_query);

    // Add labels to the nodes1
    const label_query = svg_query.selectAll(null)
        .data(nodes0)
        .enter()
        .append("text")
        .text(d => d.name)
        .attr("font-family", "Arial")
        .attr("font-size", 12)
        .attr("fill", "#000")
        .attr('x', d => -d.name.length * 3)
        .attr('y', 5)
        .attr("pointer-events", "none");

    // Create the arrowhead marker definition
    svg_query.append("defs").selectAll("marker")
        .data(["arrowhead"])
        .enter().append("marker")
        .attr("id", String)
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", 15)
        .attr("refY", -1.5)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")
        .append("path")
        .attr("d", "M0,-5L10,0L0,5");



    // Add hovering styles for nodes1 and links
    node_query.on("mouseover", function () {
        d3.select(this).attr("stroke-width", 4);
    }).on("mouseout", function () {
        d3.select(this).attr("stroke-width", 2);
    });

    // link_query.on("mouseover", function () {
    //     d3.select(this).attr("stroke-width", 3);
    // }).on("mouseout", function () {
    //     d3.select(this).attr("stroke-width", 1);
    // });

    // Start the simulation
    simulation_query.on("tick", ticked_query);
    function ticked_query() {
        link_query
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node_query
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        label_query
            .attr('x', d => d.x + 15)
            .attr('y', d => d.y);
    }

    // Define the click function
    // function click_query(d) {
    //     d3.selectAll("circle").attr("fill", "#ccc");
    //     d3.select(this).attr("fill", "orange");
    //     d3.select("#description_query").text(d.description);
    // }

    // Define the dragging functions
    function dragstarted_query(d) {
        if (!d3.event.active) simulation_query.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged_query(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended_query(d) {
        if (!d3.event.active) simulation_query.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

}


