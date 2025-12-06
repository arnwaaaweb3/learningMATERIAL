// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract SimpleStorage {
    // 1. Variabel 'data' disimpan di dalam storage (persistent)
    uint256 public data;

    // 2. Fungsi untuk menyimpan data (mengubah state/status contract)
    function set(uint256 _data) public {
        data = _data;
    }

    // 3. Fungsi untuk mengambil data (hanya melihat state, tidak mengubah)
    // view: tidak menghabiskan gas (hanya membaca data di blockchain)
    function get() public view returns (uint256) {
        return data;
    }
}