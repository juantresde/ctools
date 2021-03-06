def edge_rotate(edge, ccw=False):
    """Rotate the edge and return the newly created edge.
                        If rotating the edge fails, None will be returned.
    
    :param edge: The edge to rotate.
    :type edge: bmesh.types.BMEdge
    :param ccw: When True the edge will be rotated counter clockwise.
    :type ccw: bool
    :return: The newly rotated edge.
    :rtype: bmesh.types.BMEdge
    """


def edge_split(edge, vert, fac):
    """Split an edge, return the newly created data.
    
    :param edge: The edge to split.
    :type edge: bmesh.types.BMEdge
    :param vert: One of the verts on the edge, defines the split direction.
    :type vert: bmesh.types.BMVert
    :param fac: The point on the edge where the new vert will be created [0 - 1].
    :type fac: float
    :return: The newly created (edge, vert) pair.
    :rtype: tuple
    """


def face_flip(faces):
    """Flip the faces direction.
    
    :param face: Face to flip.
    :type face: bmesh.types.BMFace
    """


def face_join(faces, remove=True):
    """Joins a sequence of faces.
    
    :param faces: Sequence of faces.
    :type faces: bmesh.types.BMFace
    :param remove: Remove the edges and vertices between the faces.
    :type remove: bool
    :return: The newly created face or None on failure.
    :rtype: bmesh.types.BMFace
    """


def face_split(face, vert_a, vert_b, coords=(), use_exist=True, example=None):
    """Face split with optional intermediate points.
    
    :param face: The face to cut.
    :type face: bmesh.types.BMFace
    :param vert_a: First vertex to cut in the face (face must contain the vert).
    :type vert_a: bmesh.types.BMVert
    :param vert_b: Second vertex to cut in the face (face must contain the vert).
    :type vert_b: bmesh.types.BMVert
    :param coords: Optional argument to define points inbetween vert_a and vert_b.
        (type: sequence of float triplets)
    :type coords: collections.Sequence
    :param use_exist: .Use an existing edge if it exists (Only used when coords argument is empty or omitted)
    :type use_exist: bool
    :param example: Newly created edge will copy settings from this one.
    :type example: bmesh.types.BMEdge
    :return: The newly created face or None on failure.
    :rtype: (bmesh.types.BMFace, bmesh.types.BMLoop) pair
    """


def face_split_edgenet(face, edgenet):
    """Splits a face into any number of regions defined by an edgenet.
    
    :param face: The face to split.
    :type face: bmesh.types.BMFace
    :param face: The face to split.
    :param edgenet: Sequence of edges.
    :type edgenet: bmesh.types.BMEdge
    :return: The newly created faces.
    :rtype: tuple of (bmesh.types.BMFace)
    """


def face_vert_separate(face, vert):
    """Rip a vertex in a face away and add a new vertex.
    <Note> This is the same as loop_separate, and has only been added for convenience.
    
    :param face: The face to separate.
    :type face: bmesh.types.BMFace
    :param vert: A vertex in the face to separate.
    :type vert: bmesh.types.BMVert
    :return: vert
        The newly created vertex or None on failure.
    :rtype: tuple
    :param : (type: bmesh.types.BMVert)
    :rtype: tuple
    """


def loop_separate(loop):
    """Rip a vertex in a face away and add a new vertex.
    
    :param loop: The loop to separate.
    :type loop: bmesh.types.BMLoop
    :return: vert
        The newly created vertex or None on failure.
    :rtype: tuple
    :param : (type: bmesh.types.BMVert)
    :rtype: tuple
    """


def vert_collapse_edge(vert, edge):
    """Collapse a vertex into an edge.
    
    :param vert: The vert that will be collapsed.
    :type vert: bmesh.types.BMVert
    :param edge: The edge to collapse into.
    :type edge: bmesh.types.BMEdge
    :return: The resulting edge from the collapse operation.
    :rtype: bmesh.types.BMEdge
    """


def vert_collapse_faces(vert, edge, fac, join_faces):
    """Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.
    
    :param vert: The vert that will be collapsed.
    :type vert: bmesh.types.BMVert
    :param edge: The edge to collapse into.
    :type edge: bmesh.types.BMEdge
    :param fac: The factor to use when merging customdata [0 - 1].
    :type fac: float
    :return: The resulting edge from the collapse operation.
    :rtype: bmesh.types.BMEdge
    """


def vert_dissolve(vert):
    """Dissolve this vertex (will be removed).
    
    :param vert: The vert to be dissolved.
    :type vert: bmesh.types.BMVert
    :return: True when the vertex dissolve is successful.
    :rtype: bool
    """


def vert_separate(vert, edges):
    """Separate this vertex at every edge.
    
    :param vert: The vert to be separated.
    :type vert: bmesh.types.BMVert
    :param edges: The edges to separated.
    :type edges: bmesh.types.BMEdge
    :return: The newly separated verts (including the vertex passed).
    :param : (type: tuple of bmesh.types.BMVert)
    :rtype: tuple
    """


def vert_splice(vert, vert_target):
    """Splice vert into vert_target.
    <Note> The verts mustn't share an edge or face.
    
    :param vert: The vertex to be removed.
    :type vert: bmesh.types.BMVert
    :param vert_target: The vertex to use.
    :type vert_target: bmesh.types.BMVert
    """
