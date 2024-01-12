export async function deleteProject(project_id) {
  const url = `http://localhost:9999/admin/project/${project_id}`;
  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to delete project. Status: ${response.status}`);
    }

    console.log(`Project with ID ${project_id} deleted successfully`);
  } catch (error) {
    console.error("Error deleting project:", error.message);
    throw error;
  }
}
