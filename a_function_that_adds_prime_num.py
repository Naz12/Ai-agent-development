
def sum_primes(limit: int) -> int:
    """Return the sum of all prime numbers less than or equal to ``limit``.

    Description
    -----------
    Computes the sum of every prime number in the inclusive range
    ``[2, limit]`` using the Sieve of Eratosthenes. A bytearray is used
    as a compact boolean sieve for efficiency, and composite multiples
    are eliminated by slice-assignment, which is substantially faster
    than a per-element Python loop.

    Parameters
    ----------
    limit : int
        The inclusive upper bound for the prime search. Must be an
        integer. Non-integer inputs raise a ``TypeError`` (raised
        implicitly by the comparison/``range`` operations).

    Returns
    -------
    int
        The sum of all primes ``p`` such that ``2 <= p <= limit``.
        Returns ``0`` when ``limit < 2`` (i.e., there are no primes
        in the range).

    Examples
    --------
    >>> sum_primes(10)
    17          # 2 + 3 + 5 + 7
    >>> sum_primes(2)
    2
    >>> sum_primes(20)
    77          # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19
    >>> sum_primes(1)
    0
    >>> sum_primes(0)
    0

    Edge Cases
    ----------
    * ``limit < 2`` (including negative numbers, ``0``, and ``1``):
      returns ``0`` because no primes exist below ``2``.
    * ``limit == 2``: returns ``2`` (the smallest prime).
    * ``limit == 3``: returns ``5`` (2 + 3).
    * Very large ``limit``: memory scales as ``O(limit)`` bytes
      (one byte per integer); time is ``O(limit * log(log(limit)))``.
      For instance, ``sum_primes(2_000_000)`` returns ``142913828922``.
    * Non-integer ``limit`` (e.g., ``float``): raises ``TypeError``.

    Notes
    -----
    The sieve is initialized with ``sieve[i] == 1`` meaning "presumed
    prime", and indices ``0`` and ``1`` are explicitly set to ``0``.
    For each prime ``p`` discovered up to ``sqrt(limit)``, all multiples
    starting at ``p * p`` are marked composite.
    """
    if limit < 2:
        return 0

    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'

    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:limit + 1:p] = b'\x00' * (((limit - start) // p) + 1)

    return sum(i for i in range(2, limit + 1) if sieve[i])

