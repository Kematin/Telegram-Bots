import React from "react";
import { getProjects } from "../../utils/getProjects.js";
import ProjectTable from "../../components/ProjectTable/ProjectTable.jsx";

const projects = await getProjects();
function Projects() {
  return (
    <div className="projects-page">
      <ProjectTable projects={projects} />
    </div>
  );
}

export default Projects;
