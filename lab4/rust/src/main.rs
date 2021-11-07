use std::collections::HashMap;
use sha2::{Digest, Sha256};
use sha2::digest::{DynDigest, Reset};
use rand::{Rng, RngCore};

fn main() {
    println!("Hello, world!");
    let mut map: HashMap<&[u8], &[u8]> = HashMap::new();

    let hasher = Sha256::new();
    loop {
        hasher.reset();
        let random_bytes: &mut [u8; 16] = &mut [0; 16];
        rand::thread_rng().fill_bytes(random_bytes);
        hasher.update(random_bytes);
        let result = hasher.finalize();
        if map.contains_key()
        map.insert(result.as_slice().slice(0, 4), random_bytes);
    }

}
