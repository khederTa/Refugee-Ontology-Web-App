const nodes = [
    { "name": "Integration",         "description": "Refugee level of integration in her host place/country." },
    { "name": "CulturalIntegration", "description": "Cultural integration refers to the ability of refugees to talk the local langauge and to embrace or harmonize their values with those of the host place." },
    { "name": "EconomicIntegration", "description": "Economic integration is the ability of refugee to be active in the job market in the host place/country." },
    { "name": "SocialIntegration",   "description": "Social integration is the ability of refugees to build a wide and deep social network in the host country." },
    { "name": "Place",               "description": "country, city, etc." },
    { "name": "HomePlace",           "description": "It is the original country of the refugee." },
    { "name": "HostPlace",           "description": "It is the original country of the refugee." },
    { "name": "RefAgency",           "description": "Refugee Agency is the capability of refugees to act, to choose, to be as they believe that will serve their well-being the best. It is, in othre words, to be autonomous." },
    { "name": "HighAgency",          "description": "A refugee is highly autonomous; able; capable, powerful to carve out her fate and livelihood." },
    { "name": "LowAgency",           "description": "A refugee is barely autonomous; able; capable, powerful to carve out her fate and livelihood." },
    { "name": "RefIdentity",         "description": "Refugee’s, as an individual,identity." },
    { "name": "Attachment",          "description": "Attachement is always to a place; to which extent a refugee is attached to a place as a part of her identity." },
    { "name": "HomeAttachment",      "description": "Refugee is attached to places that are related to or located in her home." },
    { "name": "HostAttachment",      "description": "Refugee is attached to places that are related to or located in her host place/country." },
    { "name": "Belonging",           "description": "Belonging is generally to a group; to which extent a refugee is self-identified as a member of x group (national, religious, ethnic, etc.)." },
    { "name": "HomeBelonging",       "description": "Belonging is to groups that reside in the original country, the home. " },
    { "name": "HostBelonging",       "description": "Belonging is to groups that reside in the host country." },
    { "name": "PlaceMaking",         "description": "How a refugee forms a place that she desires to live in; what is this place? her home? her host? neither?" },
    { "name": "HomeMaking",          "description": "Placemaking activities are located physcially in the refugee home place or essentially related to it." },
    { "name": "HostMaking",          "description": "Placemaking activities are located physcially in the refugee host place or essentially related to it." },
    { "name": "Refugee",             "description": "A person who is under temporary protection or fully enjoys the legal definition of refugee status." },
    { "name": "Nationalized",        "description": "A refugee who has been granted the citizenship of the host country." },
    { "name": "stayee",              "description": "A refugee who stays in the host country, legally, illegally, or in another type without being nationalized." },
    { "name": "WouldBeReturnee",     "description": "A refugee who is determinant and fully willing to return." },
    { "name": "Transnationalism",    "description": "Activities of refugees that link or bridge multiple places together, home and host. These activities or practices can be endorsed at the everyday level or in the long term." },
    { "name": "Reintegration",       "description": "It is the ability of those who return to re-establsih their lives in their countries of origin." },
    { "name": "EconomicWellBeing",   "description": "The ability of a returnee to active in her home again." },
    { "name": "PoliticalProcess",    "description": "The ability of returnee to enjoy stable (at least) political environment in her home." },
    { "name": "SocialCapital",       "description": "The social network, social capital, that a returnee has in her home." }
    
]

const edges = [
    { "source": "CulturalIntegration", "target": "Integration",      "relationship": "SubClassOf" },
    { "source": "EconomicIntegration", "target": "Integration",      "relationship": "SubClassOf" },
    { "source": "SocialIntegration",   "target": "Integration",      "relationship": "SubClassOf" },
    { "source": "HomePlace",           "target": "Place",            "relationship": "SubClassOf" },
    { "source": "HostPlace",           "target": "Place",            "relationship": "SubClassOf" },
    { "source": "HighAgency",          "target": "RefAgency",        "relationship": "SubClassOf" },
    { "source": "LowAgency",           "target": "RefAgency",        "relationship": "SubClassOf" },
    { "source": "Attachment",          "target": "RefIdentity",      "relationship": "SubClassOf" },
    { "source": "HomeAttachment",      "target": "Attachment",       "relationship": "SubClassOf" },
    { "source": "HostAttachment",      "target": "Attachment",       "relationship": "SubClassOf" },
    { "source": "Belonging",           "target": "RefIdentity",      "relationship": "SubClassOf" },
    { "source": "HomeBelonging",       "target": "Belonging",        "relationship": "SubClassOf" },
    { "source": "HostBelonging",       "target": "Belonging",        "relationship": "SubClassOf" },
    { "source": "PlaceMaking",         "target": "RefIdentity",      "relationship": "SubClassOf" },
    { "source": "HomeMaking",          "target": "PlaceMaking",      "relationship": "SubClassOf" },
    { "source": "HostMaking",          "target": "PlaceMaking",      "relationship": "SubClassOf" },
    { "source": "Nationalized",        "target": "Refugee",          "relationship": "SubClassOf" },
    { "source": "stayee",              "target": "Refugee",          "relationship": "SubClassOf" },
    { "source": "WouldBeReturnee",     "target": "Refugee",          "relationship": "SubClassOf" },
    { "source": "EconomicWellBeing",   "target": "Reintegration",    "relationship": "SubClassOf" },
    { "source": "PoliticalProcess",    "target": "Reintegration",    "relationship": "SubClassOf" },
    { "source": "SocialCapital",       "target": "Reintegration",    "relationship": "SubClassOf" },
    { "source": "Refugee",             "target": "RefAgency",        "relationship": "HasAgency" },
    { "source": "Refugee",             "target": "Reintegration",    "relationship": "HasExpectedLevelOfReintegration" },
    { "source": "Refugee",             "target": "Place",            "relationship": "HasHome" },
    { "source": "Refugee",             "target": "Integration",      "relationship": "HasLevelOfIntegration" },
    { "source": "Refugee",             "target": "Transnationalism", "relationship": "PracticeTransnationalism" },
    { "source": "Refugee",             "target": "RefIdentity",      "relationship": "BelongTo"}
]

const svg = d3.select("#main-graph");
const width = +svg.attr("width");
const height = +svg.attr("height");

// Create the simulation with the desired forces
const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(edges).id(d => d.name).distance(50))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

// Create the links and add them to the SVG
const link = svg.append("g")
    .attr("stroke", "#999")
    .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(edges)
    .join("line")
    .attr("class", "edge")
    .attr("stroke-width", 2);


// Create the nodes and add them to the SVG

const node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
    .attr("r", 10)
    .attr("fill", "#ccc")
    .attr("stroke", "#fff")
    .attr("stroke-width", 2)
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended))
    .on("click", click);

// Add labels to the nodes


const label = svg.selectAll(null)
    .data(nodes)
    .enter()
    .append("text")
    .text(d => d.name)
    .attr("font-family", "Arial")
    .attr("font-size", 10)
    .attr("fill", "#000")
    .attr('x', d => -d.name.length * 3)
    .attr('y', 5)
    .attr("pointer-events", "none")
    .attr("text-anchor", "middle");

// Create the arrowhead marker definition
svg.append("defs").selectAll("marker")
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

// Define the dragging functions
function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

// Define the click function
function click(d) {
    d3.selectAll("circle").attr("fill", "#ccc");
    d3.select(this).attr("fill", "orange");
    d3.select("#description").text(d.name+": " +d.description);
}

// Add hovering styles for nodes and links
node.on("mouseover", function () {
    d3.select(this).attr("stroke-width", 4);
}).on("mouseout", function () {
    d3.select(this).attr("stroke-width", 2);
});

link.on("mouseover", function () {
    d3.select(this).attr("stroke-width", 3);
}).on("mouseout", function () {
    d3.select(this).attr("stroke-width", 1);
});

// Start the simulation
simulation.on("tick", ticked);

function ticked() {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);

    label
        .attr('x', d => d.x + 15)
        .attr('y', d => d.y);
}