## Rust app for Linux or RISC-V targets
### Pre-requisites
Build the Rust Docker image 
```console
docker build -t rust -f rust.Dockerfile .
docker run --rm -ti  -v $(pwd):/usr/src/vnd-boilerplate -w /usr/src/vnd-boilerplate rust:latest
```

### Building
#### For RISC-V target
```console
cargo build --release
```
#### For Linux aarch64 (Mac M1/M2) target
```console
cargo build --release --target aarch64-unknown-linux-gnu
```
#### For Linux x86_64 target
```console
cargo build --release --target x86_64-unknown-linux-gnu
```

### Testing (Linux only)
Tests are ran on native thanks to `libspeculos.so`.

`--test-threads=1` is required because `libspeculos.so` isn't thread safe.
#### For Linux aarch64 target
```console
docker run --rm -ti  -v $(pwd):/usr/src/vanadium -w /usr/src/vanadium rust:latest
cd app/rust
cargo test --target aarch64-unknown-linux-gnu -- --test-threads=1
```
#### For Linux x86_64 target
```console
docker run --rm -ti  -v $(pwd):/usr/src/vanadium -w /usr/src/vanadium rust:latest
cd app/rust
cargo test --target x86_64-unknown-linux-gnu -- --test-threads=1
```
## Notes

- Find which functions take the most of space with `cargo install bloat && cargo bloat --release -n 10`
