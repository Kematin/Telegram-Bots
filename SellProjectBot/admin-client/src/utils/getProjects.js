const categories = {
  1: "Full 11",
  2: "Full 9",
  3: "Minimum",
};
const options = {
  year: "numeric",
  month: "long",
  day: "numeric",
  hour: "numeric",
  minute: "numeric",
};

function changeCategory(project) {
  const categoryId = project.category;
  project.category = categories[categoryId];
}
function changeDatetime(project) {
  const dateTime = new Date(project.created_at);
  const formattedDateTime = dateTime.toLocaleDateString("en-US", options);
  project.created_at = formattedDateTime;
}
function changeCurrency(project) {
  const price = project.price;
  project.price = `${price} ₽`;
}

export async function getProjects() {
  const url = "http://localhost:9999/admin/projects";
  const response = await fetch(url);
  const data = await response.json();
  data.projects.forEach((project) => {
    changeCategory(project);
    changeDatetime(project);
    changeCurrency(project);
  });

  return data.projects;
}

export async function getProjectsCategory(category) {
  const url = `http://localhost:9999/admin/projects?category=${category}`;
  const response = await fetch(url);
  const data = await response.json();
  data.projects.forEach((project) => {
    changeCategory(project);
    changeDatetime(project);
    changeCurrency(project);
  });

  return data.projects;
}

export async function getProject(project_id) {
  const url = `http://localhost:9999/admin/project/${project_id}`;
  const response = await fetch(url);
  const data = await response.json();
  changeCategory(data.project);
  changeDatetime(data.project);
  changeCurrency(data.project);

  return data.project;
}

export function getFile(fileName, type, typeResponse, projectId) {
  fetch(`http://localhost:9999/admin/files/${projectId}?type=${type}`).then(
    (response) => {
      response.arrayBuffer().then((buffer) => {
        const link = document.createElement("a");
        link.download = fileName;
        const blob = new Blob([buffer], {
          type: typeResponse,
        });
        link.href = URL.createObjectURL(blob);
        link.click();
        URL.revokeObjectURL(link.href);
      });
    }
  );
}
