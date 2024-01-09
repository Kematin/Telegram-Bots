async function getProjects() {
  const url = "http://localhost:9999/admin/projects";
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

const data = await getProjects();

export default data.projects;
