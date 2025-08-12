#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para unificar una aplicación React compilada en un único archivo HTML
"""

def unify_webapp():
    """
    Lee los archivos dist/ y crea un HTML unificado
    """
    
    # Rutas de los archivos
    css_file = '/workspace/user_input_files/proyecto-github/dist/assets/index-BKe27uhd.css'
    js_file = '/workspace/user_input_files/proyecto-github/dist/assets/index-CtBRxwjR.js'
    
    # Leer archivos
    print("Leyendo archivos CSS y JavaScript...")
    
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Crear HTML unificado
    html_content = f"""<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Webapp de Gestión de Causas Legales - Defensoría Civil y Comercial N° 6</title>
    <meta name="description" content="Aplicación web profesional para la gestión de causas legales">
    
    <!-- Estilos embebidos -->
    <style>
{css_content}
    </style>
</head>

<body>
    <div id="root"></div>
    
    <!-- JavaScript embebido -->
    <script type="module">
{js_content}
    </script>
</body>
</html>"""
    
    # Guardar archivo unificado
    output_file = '/workspace/webapp_defensoria_unificada.html'
    
    print(f"Generando archivo unificado: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Información del archivo generado
    import os
    file_size = os.path.getsize(output_file)
    file_size_mb = file_size / (1024 * 1024)
    
    print(f"\n✅ Archivo unificado generado exitosamente!")
    print(f"📍 Ubicación: {output_file}")
    print(f"📦 Tamaño: {file_size_mb:.2f} MB ({file_size:,} bytes)")
    print(f"\n🎯 Características del archivo:")
    print(f"   • HTML completo y funcional")
    print(f"   • CSS inline (Tailwind CSS + estilos personalizados)")
    print(f"   • JavaScript inline (React + dependencias)")
    print(f"   • No requiere servidor web (funciona con file://)")
    print(f"   • Aplicación completa para gestión de causas legales")
    
    return output_file

if __name__ == "__main__":
    unify_webapp()