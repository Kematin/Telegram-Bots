export function addProject(data) {
  const apiUrl = "http://localhost:9999/admin/project";
  const response = fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response;
}

export function addFiles(projectId, files) {
  const apiUrl = `http://localhost:9999/admin/files/${projectId}`;

  const data = new FormData();

  data.append("doc_file", files.doc_file);
  if (files.pptx_file) {
    data.append("pptx_file", files.pptx_file);
  }
  if (files.unique_file) {
    data.append("unique_file", files.unique_file);
  }

  if (files.product_files) {
    files.product_files.forEach((productFile, index) => {
      data.append(`product_files`, productFile);
    });
  }

  fetch(apiUrl, {
    method: "POST",
    body: data,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
