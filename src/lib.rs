use pyo3::prelude::*;
/// add(a: int, b: int)
/// --
/// 
/// Formats the sum of two numbers as string.
/// 
/// Parameters
/// ----------
/// a : int
///     Integer being added
/// b : int
///     Integer 2 being added
/// Returns
/// -------
/// str
///     a + b then converted to a string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn hello_pyo3(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)
}

pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
