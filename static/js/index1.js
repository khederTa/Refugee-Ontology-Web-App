const nodes = [
    { "name": "Integration" },
    { "name": "CulturalIntegration" },
    { "name": "EconomicIntegration" },
    { "name": "SocialIntegration" },
    { "name": "Place" },
    { "name": "HomePlace" },
    { "name": "HostPlace" },
    { "name": "RefAgency" },
    { "name": "HighAgency" },
    { "name": "LowAgency" },
    { "name": "RefIdentity" },
    { "name": "Attachment" },
    { "name": "HomeAttachment" },
    { "name": "HostAttachment" },
    { "name": "Belonging" },
    { "name": "HomeBelonging" },
    { "name": "HostBelonging" },
    { "name": "PlaceMaking" },
    { "name": "HomeMaking" },
    { "name": "HostMaking" },
    { "name": "Refugee" },
    { "name": "Transnationalism" },
    { "name": "Reintegration" },
    { "name": "EconomicWellBeing" },
    { "name": "PoliticalProcess" },
    { "name": "SocialCapital" }

]

const edges = [
    { "source": "CulturalIntegration", "target": "Integration", "relationship": "SubClassOf" },
    { "source": "EconomicIntegration", "target": "Integration", "relationship": "SubClassOf" },
    { "source": "SocialIntegration", "target": "Integration", "relationship": "SubClassOf" },
    { "source": "HomePlace", "target": "Place", "relationship": "SubClassOf" },
    { "source": "HostPlace", "target": "Place", "relationship": "SubClassOf" },
    { "source": "HighAgency", "target": "RefAgency", "relationship": "SubClassOf" },
    { "source": "LowAgency", "target": "RefAgency", "relationship": "SubClassOf" },
    { "source": "Attachment", "target": "RefIdentity", "relationship": "SubClassOf" },
    { "source": "HomeAttachment", "target": "Attachment", "relationship": "SubClassOf" },
    { "source": "HostAttachment", "target": "Attachment", "relationship": "SubClassOf" },
    { "source": "Belonging", "target": "RefIdentity", "relationship": "SubClassOf" },
    { "source": "HomeBelonging", "target": "Belonging", "relationship": "SubClassOf" },
    { "source": "HostBelonging", "target": "Belonging", "relationship": "SubClassOf" },
    { "source": "PlaceMaking", "target": "RefIdentity", "relationship": "SubClassOf" },
    { "source": "HomeMaking", "target": "PlaceMaking", "relationship": "SubClassOf" },
    { "source": "HostMaking", "target": "PlaceMaking", "relationship": "SubClassOf" },
    // { "source": "Nationalized", "target": "Refugee", "relationship": "SubClassOf" },
    // { "source": "stayee", "target": "Refugee", "relationship": "SubClassOf" },
    // { "source": "WouldBeReturnee", "target": "Refugee", "relationship": "SubClassOf" },
    { "source": "EconomicWellBeing", "target": "Reintegration", "relationship": "SubClassOf" },
    { "source": "PoliticalProcess", "target": "Reintegration", "relationship": "SubClassOf" },
    { "source": "SocialCapital", "target": "Reintegration", "relationship": "SubClassOf" },
    { "source": "Refugee", "target": "RefAgency", "relationship": "HasAgency" },
    { "source": "Refugee", "target": "Reintegration", "relationship": "HasExpectedLevelOfReintegration" },
    { "source": "Refugee", "target": "Place", "relationship": "HasHome" },
    { "source": "Refugee", "target": "Integration", "relationship": "HasLevelOfIntegration" },
    { "source": "Refugee", "target": "Transnationalism", "relationship": "PracticeTransnationalism" },
    { "source": "Refugee", "target": "RefIdentity", "relationship": "BelongTo" }
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
    .attr("stroke", "#8ec2fd")
    .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(edges)
    .join("line")
    .attr("class", "edge")
    .attr("stroke-width", 3)
    .attr('title', d => d.relationship);


// Create the nodes and add them to the SVG

const node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
    .attr("r", 10)
    .attr("fill", "#DDD")
    .attr("stroke", "#fff")
    .attr("stroke-width", 3)
    .attr('title', d => d.relationship)
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
    .attr("fill", "#31323d")
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
    d3.selectAll("circle").attr("fill", "#ddd");
    d3.select(this).attr("fill", "#6eb2ff");
    // d3.select("#description").text(d.name+": " +d.description);
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
    d3.select(this).attr("stroke-width", 2);
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