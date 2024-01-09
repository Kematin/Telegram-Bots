import React from "react";
import projects from "../../utils/getProjects.js";

function Projects() {
  return projects.map((project, index) => {
    return <h1 key={index}>{project.name}</h1>;
  });
}

export default Projects;
