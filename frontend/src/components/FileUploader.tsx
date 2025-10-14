import { useState } from "react";
import Styles from "../styles/pages/Home.module.css";
import api from "../api.js";

type UploadStatus = 'idle' | 'uploading' | 'success' | 'error';

export default function FileUploader() {
    
    const [file, setFile] = useState<File | null>(null);
    const [status, setStatus] = useState<UploadStatus>('idle');

    function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
        if (event.target.files && event.target.files.length > 0) {
            setFile(event.target.files[0] ?? null);
            if (event.target.files[0]) {
                handleFileUpload(event.target.files[0]);
            } else {
                console.error("No file selected");
            }
        }
    }

    async function handleFileUpload(file: File) {
        console.log("Uploading file:", file);
        if (!file) {
            console.error("No file selected for upload.");
            return;
        }

        setStatus('uploading');
        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await api.post('/api/image/', formData, {
                headers: { 
                    'Content-Type': 'multipart/form-data' ,
                    'Authorization': `Bearer ${localStorage.getItem('ACCESS_TOKEN')}`
                }  
            });
            if (response.status === 200) {
                setStatus('success');
                console.log("File uploaded successfully:", response.data);
            } else {
                setStatus('error');
                console.error("File upload failed");
            }
        } catch (error) {
            setStatus('error');
            console.error("File upload error:", error);
        }
    }
    return (
        <div>
            <input
                onChange={handleFileChange}
                className={Styles.ctaButton}
                type="file"
                id="fileInput"
                accept="image/*"
                style={{ display: 'none' }}
            />
            <label htmlFor="fileInput" className={Styles.ctaButton}>Upload Image</label>
        </div>
    );
}