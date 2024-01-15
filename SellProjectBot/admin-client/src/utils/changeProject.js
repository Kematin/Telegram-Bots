export function changeProject(data, projectId) {
  try {
    const response = fetch(`http://localhost:9999/admin/project/${projectId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then((response) => {
      return response;
    });
    return response;
  } catch (error) {
    console.error("Error updating project:", error);
    throw error;
  }
}

export function changeFiles(projectId, files) {
  const apiUrl = `http://localhost:9999/admin/files/${projectId}`;
  let response = Promise;

  const data = new FormData();
  let count = 0;
  if (files.doc_file && files.doc_file !== "HAVE") {
    data.append("doc_file", files.doc_file);
  } else {
    count++;
  }
  if (files.pptx_file && files.pptx_file !== "HAVE") {
    data.append("pptx_file", files.pptx_file);
  } else {
    count++;
  }
  if (files.unique_file && files.unique_file !== "HAVE") {
    data.append("unique_file", files.unique_file);
  } else {
    count++;
  }

  if (files.product_files && files.product_files !== "HAVE") {
    files.product_files.forEach((productFile) => {
      data.append(`product_files`, productFile);
    });
  } else {
    count++;
  }

  if (count !== 4) {
    console.log("CHANGE PROJECT FILES");
    response = fetch(apiUrl, {
      method: "PUT",
      body: data,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        return data;
      })
      .catch((error) => {
        console.error("Error:", error);
        return error;
      });
  }
  return response;
}
