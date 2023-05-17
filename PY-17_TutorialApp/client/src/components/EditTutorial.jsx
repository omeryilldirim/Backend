import axios from "axios";
import { useEffect, useState } from "react";



const EditTutorial = ({getTutorials, editItem}) => {
  const { id, title: newTitle, description: newDescription } = editItem;

  const [title, setTitle] = useState(newTitle);
  const [description, setDescription] = useState(newDescription);

  useEffect(() => {
    setTitle(newTitle);
    setDescription(newDescription);
  }, [newTitle, newDescription]);

  const editTutorial = async (id, tutor) => {
    const url = "http://127.0.0.1:8000/tutorials";
    try {
      await axios.put(`${url}/${id}/`, tutor);
    } catch (error) {
      console.log(error);
    }
    getTutorials();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    editTutorial(id, { title, description });
    setTitle("");
    setDescription("");
  };
  
  // const handleSaveChanges = ()=>{
  //   editTutorial({id,title,description});
  // }
  // const handleTitleChange = (e)=>{
  //   setTitle(e.target.value)
  // }
  // const handleDescriptionChange = (e)=>{
  //   setDescription(e.target.value)
  // }

  return (
    <div className="modal" tabIndex="-1" id="edit-tutor">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Edit Tutorial</h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">
            <form onSubmit={handleSubmit}>
              <label className="form-label" htmlFor="title">Title</label>
              <input className="form-control mb-3" type="text" name="title" id="title" value={title || ""} 
              onChange={(e) => setTitle(e.target.value)}
              />
              <label className="form-label"  htmlFor="desc">Description</label>
              <input className="form-control" type="text" name="desc" id="desc" value={description || ""}
              onChange={(e) => setDescription(e.target.value)}
               />
            </form>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button type="button" className="btn btn-primary" data-bs-dismiss="modal"
            onClick={handleSubmit}
            >
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default EditTutorial
