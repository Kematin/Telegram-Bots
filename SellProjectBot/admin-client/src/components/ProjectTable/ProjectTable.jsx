import "./index.css";
import { NavLink } from "react-router-dom";
import ChangeProject from "../ChangeProject/ChangeProject";
import ModalProject from "../ModalProject/ModalProject";
import React, { useState, useEffect } from "react";
import { getProject } from "../../utils/getProjects";
import { deleteProject } from "../../utils/deleteProject";

function TheadTh({ name }) {
  return (
    <th className="px-5 py-4 text-left uppercase table-header-text ">{name}</th>
  );
}

function TbodyTd({ name, project_id }) {
  if (project_id) {
    return (
      <td className="table-main-text px-6 py-4 whitespace-nowrap">
        <NavLink to={`/project/${project_id}`}>{name}</NavLink>
      </td>
    );
  } else {
    return (
      <td className="table-main-text px-6 py-4 whitespace-nowrap">{name}</td>
    );
  }
}

function TbodyBool({ status }) {
  if (status) {
    return (
      <td className="px-6 py-4 items-center whitespace-nowrap boolean-status">
        <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
          Есть
        </span>
      </td>
    );
  } else {
    return (
      <td className="px-6 py-4 items-center whitespace-nowrap boolean-status">
        <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
          Нет
        </span>
      </td>
    );
  }
}

function ReturnChangeProject({ project_id, isModal, setModal }) {
  const [project, setProject] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const projectData = await getProject(project_id);
        setProject(projectData);
      } catch (error) {
        console.error("Error fetching project:", error);
      }
    };

    fetchData();
  }, [project_id]);

  if (!project) {
    return <div>Loading...</div>;
  }

  return (
    <ModalProject
      isVisible={isModal}
      title={project.name}
      content={<ChangeProject project={project} />}
      footer={project.created_at}
      onClose={() => setModal(false)}
    />
  );
}

function ActionButton({ project_id }) {
  const [isModal, setModal] = React.useState(false);
  const openModal = () => {
    setModal(!isModal);
  };
  return (
    <td className="px-6 py-4 whitespace-nowrap">
      <button
        onClick={openModal}
        className="px-4 py-2 font-medium text-white bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:shadow-outline-blue active:bg-blue-600 transition duration-150 ease-in-out"
      >
        Изменить
      </button>
      {isModal && (
        <ReturnChangeProject
          project_id={project_id}
          isModal={isModal}
          setModal={setModal}
        />
      )}
      <button
        onClick={async () => {
          await deleteProject(project_id);
          window.location.reload();
        }}
        className="ml-2 px-4 py-2 font-medium text-white bg-red-600 rounded-md hover:bg-red-500 focus:outline-none focus:shadow-outline-red active:bg-red-600 transition duration-150 ease-in-out"
      >
        Удалить
      </button>
    </td>
  );
}

function ProjectTable({ projects }) {
  return (
    <table className="project-table min-w-full divide-y-2 divide-gray-100 project-table">
      <thead>
        <tr>
          <TheadTh name="Имя" />
          <TheadTh name="Цена" />
          <TheadTh name="Категория" />
          <TheadTh name="Блок" />
          <TheadTh name="Презентация" />
          <TheadTh name="Продукт" />
          <TheadTh name="Уникальность" />
          <TheadTh name="Действия" />
          <TheadTh name="Дата создания" />
        </tr>
      </thead>
      <tbody className="table-body divide-gray-200">
        {projects.map((project) => {
          return (
            <tr key={project.id}>
              <TbodyTd name={project.name} project_id={project.id} />
              <TbodyTd name={project.price} />
              <TbodyTd name={project.category} />
              <TbodyBool status={project.is_blocked} />
              <TbodyBool status={project.have_presentation} />
              <TbodyBool status={project.have_product} />
              <TbodyBool status={project.have_unique} />
              <ActionButton project_id={project.id} />
              <TbodyTd name={project.created_at} />
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default ProjectTable;
