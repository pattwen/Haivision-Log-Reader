async function handleFetch(url, options = {}) {
    try {
        const response = await fetch(url, options);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.message || 'Network Request Error');
        }
        return data;
    } catch (err) {
        alert(err.message);
        throw err;
    }
}

function initUpload() {
    const fileInput = document.getElementById('file-input');
    const uploadArea = document.getElementById('upload-area');

    if (!uploadArea || !fileInput) return;

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => uploadArea.classList.add('dragover'), false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => uploadArea.classList.remove('dragover'), false);
    });

    uploadArea.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) uploadFile(files[0]);
    });

    uploadArea.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) uploadFile(fileInput.files[0]);
    });
}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    const uploadStatus = document.getElementById('upload-status');
    if (uploadStatus) uploadStatus.innerText = 'uploading...';

    try {
        const result = await handleFetch('/api/upload', {
            method: 'POST',
            body: formData
        });
        if (result.success) {
            if (uploadStatus) uploadStatus.innerText = 'Upload successful! Redirecting to the task management page...';
            setTimeout(() => {
                window.location.href = '/tasks';
            }, 2000);
        }
    } catch (error) {
        if (uploadStatus) uploadStatus.innerText = 'Upload failed：' + error.message;
    }
}

async function startAnalysis(taskId) {
    const btn = document.getElementById(`btn-analyze-${taskId}`);
    if (btn) btn.disabled = true;

    try {
        await handleFetch(`/api/tasks/${taskId}/analyze`, { method: 'POST' });
        window.location.reload();
    } catch (e) {
        if (btn) btn.disabled = false;
    }
}

async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task and all analysis data?')) return;

    try {
        await handleFetch(`/api/tasks/${taskId}`, { method: 'DELETE' });
        window.location.reload();
    } catch (e) {
        console.error(e);
    }
}

function startTasksPolling() {
    const processingElements = document.querySelectorAll('.badge-Processing');
    if (processingElements.length > 0) {
        setTimeout(() => {
            window.location.reload();
        }, 3000);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initUpload();
    startTasksPolling();
});