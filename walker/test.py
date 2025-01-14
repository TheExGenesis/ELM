from square import make_walker as make_walker_square
from radial import make_walker as make_walker_radial
from CPPN_fixed import make_walker as make_walker_cppn_fixed
from CPPN_mutable import make_walker as make_walker_cppn_mutable

# Compare to serialized square seed from paper (pg. 17) #
square_seed = make_walker_square()
square_seed_expected = {
    "joints": [(0, 0), (0, 10), (10, 10), (10, 0), (5, 5)],
    "muscles": [
    [0, 1, {"type": "distance"}],
    [1, 2, {"type": "distance"}],
    [2, 3, {"type": "distance"}],
    [3, 0, {"type": "distance"}],
    [3, 4, {"type": "distance"}],
    [0, 4, {"type": "muscle", "amplitude": 2.12, "phase": 0.0}],
    [1, 4, {"type": "muscle", "amplitude": 2.12, "phase": 0.0}],
    [2, 4, {"type": "muscle", "amplitude": 2.12, "phase": 0.0}],
    ],
}

print("Square Seed Serialization Passed: ",  square_seed == square_seed_expected)


# Print other seeds #
radial_seed = make_walker_radial()
cppn_fixed_seed = make_walker_cppn_fixed()
cppn_mutable_seed = make_walker_cppn_mutable()
print("\n Radial Seed: \n ", radial_seed)
print("\n CPPN Fixed Seed: \n ", cppn_fixed_seed)
print("\n CPPN Mutable Seed: \n ", cppn_mutable_seed)