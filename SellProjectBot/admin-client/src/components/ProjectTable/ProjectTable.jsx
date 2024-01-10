import "./index.css";
import { NavLink } from "react-router-dom";
import React from "react";

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

function ActionButton({ project_id }) {
  return (
    <td className="px-6 py-4 whitespace-nowrap">
      <button className="px-4 py-2 font-medium text-white bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:shadow-outline-blue active:bg-blue-600 transition duration-150 ease-in-out">
        Изменить
      </button>
      <button className="ml-2 px-4 py-2 font-medium text-white bg-red-600 rounded-md hover:bg-red-500 focus:outline-none focus:shadow-outline-red active:bg-red-600 transition duration-150 ease-in-out">
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
