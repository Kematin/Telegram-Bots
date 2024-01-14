export async function addProject(data) {
  const apiUrl = "http://localhost:9999/admin/project";
  const response = await fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response;
}

export function addFile(projectId, file) {}
