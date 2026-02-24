import React, { useEffect, useState } from 'react';
import { getCategories, getProducts } from './services/api';

function App() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([getProducts(), getCategories()])
      .then(([resProducts, resCategories]) => {
        const prodData = resProducts.data.results || resProducts.data;
        const catData = resCategories.data.results || resCategories.data;
        
        setProducts(Array.isArray(prodData) ? prodData : []);
        setCategories(Array.isArray(catData) ? catData : []);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Veri çekme hatası:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="p-10 text-blue-400 font-mono">Veriler yükleniyor...</div>;

  return (
    <div className="min-h-screen bg-[#0b0f1a] p-10 text-slate-300 font-sans">
      
      {/* --- ÜRÜNLER BÖLÜMÜ --- */}
      <section className="mb-16">
        <h2 className="text-2xl font-black text-white mb-6 flex items-center gap-3">
          <span className="w-1 h-8 bg-blue-500 rounded-full"></span>
          ÜRÜNLER
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {products.map((product) => (
            <div key={product.id} className="bg-slate-900/50 border border-slate-800 p-5 rounded-xl hover:bg-slate-800 transition">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-lg font-bold text-slate-100">{product.name}</h3>
                  <p className="text-sm text-slate-500 mt-1">ID: #{product.id}</p>
                </div>
                <span className="text-emerald-400 font-mono font-bold text-lg">
                  {product.price} TL
                </span>
              </div>
              {product.description && (
                <p className="mt-3 text-sm text-slate-400 italic">
                  {product.description}
                </p>
              )}
            </div>
          ))}
        </div>
      </section>

      {/* --- KATEGORİLER BÖLÜMÜ --- */}
      <section>
        <h2 className="text-2xl font-black text-white mb-6 flex items-center gap-3">
          <span className="w-1 h-8 bg-emerald-500 rounded-full"></span>
          KATEGORİLER
        </h2>
        <div className="flex flex-wrap gap-3">
          {categories.map((category) => (
            <div 
              key={category.id} 
              className="bg-slate-800 border border-slate-700 px-6 py-3 rounded-lg text-slate-200 font-semibold shadow-sm"
            >
              {category.name}
              <span className="ml-2 text-[10px] text-slate-500 font-normal">
                (ID: {category.id})
              </span>
            </div>
          ))}
        </div>
      </section>

    </div>
  );
}

export default App;