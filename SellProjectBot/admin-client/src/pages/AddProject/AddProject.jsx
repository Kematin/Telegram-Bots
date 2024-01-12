import React, { useState } from "react";
import "./index.css";

function InputField({ label, value, onChange }) {
  return (
    <div>
      <label className="label-text">{label}</label>
      <input
        className="input-field w-full py-3 border border-slate-200 rounded-lg px-3 focus:outline-none focus:border-slate-500 hover:shadow dark:bg-gray-600 dark:text-gray-100"
        value={value}
        onChange={onChange}
        type="text"
      />
    </div>
  );
}

function TextArea({ label, value, onChange }) {
  return (
    <div>
      <label className="label-text">{label}</label>
      <textarea
        value={value}
        onChange={onChange}
        className="w-full py-3 border border-slate-200 rounded-lg px-3 focus:outline-none focus:border-slate-500 hover:shadow dark:bg-gray-600 dark:text-gray-100"
      ></textarea>
    </div>
  );
}

function CheckBox({ label, isChecked, handleCheckboxChange }) {
  return (
    <label className="label-text">
      <input
        type="checkbox"
        checked={isChecked}
        onChange={handleCheckboxChange}
        className="checkbox-input mr-1"
      />
      {label}
    </label>
  );
}

function SelectFromListInput({ label, options, onChange }) {
  const [selectedValue, setSelectedValue] = useState("");

  const handleSelectChange = (event) => {
    const newValue = event.target.value;
    setSelectedValue(newValue);

    onChange(newValue);
  };

  return (
    <div className="mb-4">
      <label className="label-text">
        {label}:
        <select
          value={selectedValue}
          onChange={handleSelectChange}
          className="block w-full py-3 border border-slate-200 rounded-lg px-3 focus:outline-none focus:border-slate-500 hover:shadow dark:bg-gray-600 dark:text-gray-100"
        >
          {options.map((option) => (
            <option className="select-item" key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
}

function AddProject() {
  const [name, setName] = useState("");
  const [summary, setSummary] = useState("");
  const [price, setPrice] = useState("");
  const [checkPresentation, setPresentation] = useState(false);
  const [checkUnique, setUnique] = useState(false);
  const [checkProduct, setProduct] = useState(false);
  const [category, setCategory] = useState("minimum");
  function createProject(event) {
    event.preventDefault();
    const data = {
      name: name,
      summary: summary,
      price: price,
      category: category,
      have_presentation: checkPresentation,
      have_unique: checkUnique,
      have_product: checkProduct,
    };
    console.log(data);
    return false;
  }
  return (
    <div id="add-project-page">
      <h1>BITCH</h1>
      <div className="">
        <form onSubmit={createProject} className="max-w-2xl">
          <div className="form-border flex flex-wrap shadow rounded-lg p-3 dark:bg-transparent-600">
            <h2 className="header-2-text text-xl pb-2">Добавить проект:</h2>

            <div className="flex flex-col gap-2 w-full border-gray-400">
              <InputField
                label="Название"
                value={name}
                onChange={(event) => {
                  setName(event.target.value);
                }}
              />
              <TextArea
                label="Краткое содержание"
                value={summary}
                onChange={(event) => {
                  setSummary(event.target.value);
                }}
              />
              <InputField
                label="Цена"
                value={price}
                onChange={(event) => {
                  setPrice(event.target.value);
                }}
              />
              <div className="checkbox-combo mb-4">
                <CheckBox
                  label="Презентация"
                  isChecked={checkPresentation}
                  handleCheckboxChange={() => {
                    const newCheckedState = !checkPresentation;
                    setPresentation(newCheckedState);
                  }}
                />
                <CheckBox
                  label="Уникальность"
                  isChecked={checkUnique}
                  handleCheckboxChange={() => {
                    setUnique(!checkUnique);
                  }}
                />
                <CheckBox
                  label="Продукт"
                  isChecked={checkProduct}
                  handleCheckboxChange={() => {
                    setProduct(!checkProduct);
                  }}
                />
              </div>

              <SelectFromListInput
                label="Категория"
                options={["minimum", "full11", "full9"]}
                onChange={(selectedValue) => {
                  setCategory(selectedValue);
                }}
              />

              <div className="submit-button flex justify-end">
                <button
                  className="py-1.5 px-3 m-1 font-medium text-white bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:shadow-outline-blue active:bg-blue-600 transition duration-150 ease-in-out"
                  type="submit"
                >
                  Создать
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default AddProject;
