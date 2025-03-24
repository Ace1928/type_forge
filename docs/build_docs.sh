#!/bin/bash
# filepath: /home/lloyd/eidosian_forge/type_forge/docs/build_docs.sh

# Eidosian Type Forge Documentation Builder
# Precise, elegant documentation with modern components

set -e  # Exit on error for immediate feedback

echo "🔮 Building Eidosian Type Forge documentation with latest components"

# Apply precision fix for MyST footnote compatibility
export PYTHONNOUSERSITE=1
export PYTHONWARNINGS="ignore:Role 'sub-ref' is already registered:UserWarning"

# Clean previous build for pristine state
echo "🧹 Cleaning previous build artifacts"
rm -rf _build

# Build with explicit compatibility options
echo "⚡ Building documentation with elegant conflict resolution"
sphinx-build -b html \
  -D suppress_warnings=myst.footnote \
  -D myst_footnote_transition=1 \
  -D myst_dmath_double_inline=True \
  . _build/html

# Verify build success
if [ $? -eq 0 ] && [ -f _build/html/index.html ]; then
    echo "✅ Documentation built successfully"
    echo "📚 View your documentation at: file://$(pwd)/_build/html/index.html"
    echo "🌐 Or serve with: python -m http.server 8000 --directory _build/html"
else
    echo "❌ Documentation build failed"
    exit 1
fi
