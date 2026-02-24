import axios from 'axios';

// Backend adresin (Localhost)
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api', 
});

// Ürünleri getirme fonksiyonu (Parametre desteğiyle birlikte)
export const getProducts = (params) => api.get('/products/', { params });
export const getCategories = (params) => api.get('/categories/', { params });
export default api; // Bunu "api" olarak dışa aktarmak önemli