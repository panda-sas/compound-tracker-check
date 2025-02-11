import React, { useState, useEffect } from "react";

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/projects")
      .then((response) => response.json())
      .then((data) => setProjects(data))
      .catch((error) => console.error("Error fetching projects:", error));
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      {projects.length === 0 ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {projects.map((project) => (
            <li key={project.id}>
              {project.name} - {project.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Projects;
