# Legacy Launcher for Windows XP, 7, 8, 8.1

This directory contains a lightweight, extremely fast Rust server that bundles your Astro static site (`../dist`) into a single executable and exposes the native Win32 `Rich Text Format` (RTF) clipboard functionality over a local HTTP endpoint.

It is designed to launch a local browser (like **Supermium**, MyPal, Thorium, Chrome, or Edge) in `--app` mode, giving the illusion of a dedicated application while maintaining full support for legacy operating systems and perfect native PageMaker 7.0 compatibility.

## How to Compile

To compile for **Windows 7 / 8 / 8.1 (x86 / 32-bit)**:
*(You must use Rust 1.77, as newer versions dropped Win7 support)*
```bash
rustup install 1.77-i686-pc-windows-msvc
cargo +1.77 build --target i686-pc-windows-msvc --release
```

To compile for **Windows XP (x86 / 32-bit)**:
*(You must use an even older Rust toolchain like 1.68 or a specialized XP branch, and link with the XP subsystem)*
```bash
rustup install 1.68-i686-pc-windows-msvc
cargo +1.68 build --target i686-pc-windows-msvc --release
```

## How to Test
1. Build the Astro project first: `npm run build` from the root directory.
2. Build this project: `cargo build --release` inside `legacy-launcher`.
3. The resulting executable will automatically start a local server, hook the Win32 clipboard APIs, and attempt to launch the browser in restricted app mode.
