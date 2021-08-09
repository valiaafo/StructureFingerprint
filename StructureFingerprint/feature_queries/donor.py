# -*- coding: utf-8 -*-
#
#  Copyright 2020, 2021 Aleksandr Sizov <murkyrussian@gmail.com>
#  Copyright 2020, 2021 Ramil Nugmanov <nougmanoff@protonmail.com>
#  This file is part of StructureFingerprint.
#
#  StructureFingerprint is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from CGRtools.containers import QueryContainer
from CGRtools.periodictable import ListElement

queries = []

q = QueryContainer()
q.add_atom('N', charge=0, hybridization=4, neighbors=2)
queries.append(q)

q = QueryContainer()
q.add_atom('N', hybridization=1, hydrogens=(1, 2, 3, 4))
queries.append(q)

q = QueryContainer()
q.add_atom(ListElement(['O', 'S']), charge=0, hydrogens=1)
queries.append(q)


__all__ = ['queries']
