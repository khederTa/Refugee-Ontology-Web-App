const treeD = {
    "name": "Thing",
    "children": [
        {
            "name": "Integration",
            "description": "Active engagement of refugees in their host countries, culturally, economically, and socially. It is the opposite of exclusion, isolation, and limbo life.",
            "children": [
                {
                    "name": "Cultural Integration",
                    "description": "The refugee's ability to speak the local language and to embrace or to live in harmony with the  values of the host country."
                },
                {
                    "name": "Social Integration",
                    "description": "The refugee's ability to build a wide and deep social network in the host country, such as having friends and good relations with neighbors."
                },
                {
                    "name": "Economic Integration",
                    "description": "The refugee's ability to be active in the job market in the host place/country."
                }
            ]
        },
        {
            "name": "Place",
            "description": "The physical, environemntal, and geographical \"container\" where a refugee (or any other person) lives, acts, resides, or passes through, and [the place is] the idea or abstract notion that a refugee refers to as a site of residence,  home, or an anchor of culture. Place need not be material only. It is immaterial entity (manifesting as perception of tradition, as memory, as a definer of identity, etc.) as much as a material entity or a physical site",
            "children": [
                {
                    "name": "Host Place",
                    "description": "The place where a refugee lives. It may refer to a nation-state, city, or a village."
                },
                {
                    "name": "Home Place",
                    "description": "The place of origin from where refugees had fled. It cna be a city, a vilalge, or a nation-state."
                }
            ]
        },
        {
            "name": "Refugee Agency",
            "description": "The capability of refugees to act, to choose, to be as they believe that will serve their well-being the best. It is, in othre words, to be autonomous.",
            "children": [
                {
                    "name": "High Agency",
                    "description": "The highly autonomy, capability, and power enjoyed by a refugee in a way that makes her, even relatively, able to carve out her fate and livelihood."
                },
                {
                    "name": "Low Agency",
                    "description": "The weak autonomy, capability, and power of a refugee in a way that makes her unable to carve out her fate and livelihood."
                }
            ]
        },
        {
            "name": "Refugee Identity",
            "description": "The way a refugee defines herself; the sense of a self.",
            "children": [
                {
                    "name": "Attachment",
                    "description": "Refugee's linkage to a place; to which extent a refugee is attached to a place as a part of her identity.",
                    "children": [
                        {
                            "name": "Host Attachment",
                            "description": "Refugee's attachement to a place(s) that is related to or located in her host place/country."
                        },
                        {
                            "name": "Home Attachment",
                            "description": "Refugee's attachement to a place(s) that is related to or located in her home."
                        }
                    ]
                },
                {
                    "name": "Belonging",
                    "description": "Refugee's linkage to a group; to which extent a refugee is self-identified as a member of a group (national, religious, ethnic, etc.).",
                    "children": [
                        {
                            "name": "Host Belonging",
                            "description": "Belonging to a group(s) that resides or exists in the host country."
                        },
                        {
                            "name": "Home Belonging",
                            "description": "Belonging to a group that resides in refugees' original country (home place)."
                        }
                    ]
                },
                {
                    "name": "Place Making",
                    "description": "The way a refugee conceptualizes, understands, and struggles to form - by whatever means she has - a place where she lives or desires to live (for example, by decorating her house in a similar way to traditional houses in her home place, or by political actiivities to form a new government in home, etc.).",
                    "children": [
                        {
                            "name": "Host Making",
                            "description": "Activities that are located physcially in the refugee's host place or essentially related to it."
                        },
                        {
                            "name": "Home Making",
                            "description": "Activities that are located physcially  in the refugee's home place or essentially related to it (even if the refugee lives remotely)."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Reintegration",
            "description": "The ability of those who return to re-establsih their lives in their countries of origin.",
            "children": [
                {
                    "name": "ُEconomic Well Being",
                    "description": "The ability of a returnee to be active in her home again economically and in the job market."
                },
                {
                    "name": "Social Capital",
                    "description": "The social network, social capital, that a returnee has in her home."
                },
                {
                    "name": "Political Process",
                    "description": "The ability of returnee to enjoy stable (at least) political environment in her home."
                }
            ]
        },
        {
            "name": "Transnationalism",
            "description": "Activities of refugees that link or bridge multiple places together, home and host. These activities or practices can be endorsed at the everyday level or in the long term."
        }

    ]
};

// Set the dimensions and margins of the diagram
var margin = { top: 10, right: 45, bottom: 15, left: 45 },
    tree_width = 800;
tree_height = 500;

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var tree_svg = d3.select(".main-tree").append('svg')
    .attr("width", tree_width + margin.right + margin.left)
    .attr("height", tree_height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate("
        + margin.left + "," + margin.top + ")");

var i = 0,
    duration = 750,
    root;

// declares a tree layout and assigns the size
var treemap = d3.tree().size([tree_height, tree_width]);

// Assigns parent, children, height, depth
root = d3.hierarchy(treeD, function (d) { return d.children; });
root.x0 = tree_height / 2;
root.y0 = 0;

// Collapse after the second level
root.children.forEach(collapse);

update(root);

// show concepts defintions
function showdef(obj) {
    console.log(obj.data.name + ': ' + obj.data.description)
    d3.select("#description").text(obj.data.name + ': ' + obj.data.description);
}

// Collapse the node and all it's children
function collapse(d) {
    if (d.children) {
        d._children = d.children
        d._children.forEach(collapse)
        d.children = null
    }
}

function update(source) {

    // Assigns the x and y position for the nodes
    var treeD = treemap(root);

    // Compute the new tree layout.
    var nodes = treeD.descendants(),
        links = treeD.descendants().slice(1);

    // Normalize for fixed-depth.
    nodes.forEach(function (d) { d.y = d.depth * 180 });

    // ****************** Nodes section ***************************

    // Update the nodes...
    var node = tree_svg.selectAll('g.node')
        .data(nodes, function (d) { return d.id || (d.id = ++i); });

    // Enter any new modes at the parent's previous position.
    var nodeEnter = node.enter().append('g')
        .attr('class', 'node')
        .attr("transform", function (d) {
            return "translate(" + source.y0 + "," + source.x0 + ")";
        })
        .on('click', click);

    // Add Circle for the nodes
    nodeEnter.append('circle')
        .attr('class', 'node')
        .attr('r', 1e-6)
        .style("fill", function (d) {
            return d._children ? "lightsteelblue" : "#fff";
        });

    // Add labels for the nodes
    nodeEnter.append('text')
        .attr("dy", ".35em")
        .attr("x", function (d) {
            return d.children || d._children ? -13 : 13;
        })
        .attr("text-anchor", function (d) {
            return d.children || d._children ? "end" : "start";
        })
        .text(function (d) { return d.data.name; }).attr('class', 'pointer-class').on('click', showdef);

    // UPDATE
    var nodeUpdate = nodeEnter.merge(node);

    // Transition to the proper position for the node
    nodeUpdate.transition()
        .duration(duration)
        .attr("transform", function (d) {
            return "translate(" + d.y + "," + d.x + ")";
        });

    // Update the node attributes and style
    nodeUpdate.select('circle.node')
        .attr('r', 10)
        .style("fill", function (d) {
            return d._children ? "lightsteelblue" : "#fff";
        })
        .attr('cursor', 'pointer');


    // Remove any exiting nodes
    var nodeExit = node.exit().transition()
        .duration(duration)
        .attr("transform", function (d) {
            return "translate(" + source.y + "," + source.x + ")";
        })
        .remove();

    // On exit reduce the node circles size to 0
    nodeExit.select('circle')
        .attr('r', 1e-6);

    // On exit reduce the opacity of text labels
    nodeExit.select('text')
        .style('fill-opacity', 1e-6);

    // ****************** links section ***************************

    // Update the links...
    var link = tree_svg.selectAll('path.link')
        .data(links, function (d) { return d.id; });

    // Enter any new links at the parent's previous position.
    var linkEnter = link.enter().insert('path', "g")
        .attr("class", "link")
        .attr('d', function (d) {
            var o = { x: source.x0, y: source.y0 }
            return diagonal(o, o)
        });

    // UPDATE
    var linkUpdate = linkEnter.merge(link);

    // Transition back to the parent element position
    linkUpdate.transition()
        .duration(duration)
        .attr('d', function (d) { return diagonal(d, d.parent) });

    // Remove any exiting links
    var linkExit = link.exit().transition()
        .duration(duration)
        .attr('d', function (d) {
            var o = { x: source.x, y: source.y }
            return diagonal(o, o)
        })
        .remove();

    // Store the old positions for transition.
    nodes.forEach(function (d) {
        d.x0 = d.x;
        d.y0 = d.y;
    });

    // Creates a curved (diagonal) path from parent to the child nodes
    function diagonal(s, d) {

        path = `M ${s.y} ${s.x}
    C ${(s.y + d.y) / 2} ${s.x},
      ${(s.y + d.y) / 2} ${d.x},
      ${d.y} ${d.x}`

        return path
    }

    // Toggle children on click.
    function click(d) {
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = d._children;
            d._children = null;
        }
        update(d);
    }
}

